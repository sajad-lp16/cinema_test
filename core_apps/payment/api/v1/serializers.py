from django.db import transaction

from rest_framework import serializers

from core_apps.account.api.v1.serializers import UserSerializer
from core_apps.payment.models import Transaction
from core_apps.venue.models import Ticket
from core_apps.payment.gateways import (
    BasePaymentGateway,
    get_gateway_by_name
)


class PaymentSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = (
            "id",
            "user",
            "price",
            "status",
            "ticket",
            "gateway"
        )

    def get_status(self, instance: Transaction):
        return instance.get_status_display()

    def validate_ticket(self, ticket: Ticket):
        if not ticket.sell_ok_by_id:
            raise serializers.ValidationError("ticket is not sellable")
        return ticket

    def save(self, **kwargs):
        with transaction.atomic():
            request = self.context.get("request")
            ticket = self.validated_data.get("ticket")

            self.validated_data["user"] = request.user
            self.validated_data["price"] = ticket.price
            instance: Transaction = super().save(**kwargs)

            ticket.lock_ticket()

            gateway_name = self.validated_data.get("gateway")
            gateway_manager: BasePaymentGateway = get_gateway_by_name(gateway_name)
            payload = {"user_id": request.user.id, "transaction_id": instance.id, "ticket_id": ticket.id}
            is_ok = gateway_manager.perform_payment(price=instance.price, payload=payload)

            if not is_ok:
                raise serializers.ValidationError("Payment failed")
