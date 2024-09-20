import logging

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView
)

from core_apps.venue.models import Ticket
from core_apps.payment.models import Transaction
from core_apps.payment.gateways import get_all_gateways_name
from core_apps.payment.api.v1.permissions import IsOwnerOrAdmin
from core_apps.payment.api.v1.serializers import PaymentSerializer

User = get_user_model()
Logger = logging.getLogger("payment")


class GatewaysListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        response = {"gateways": get_all_gateways_name()}
        return Response(response, status=status.HTTP_200_OK)


class BuyTicketAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Transaction.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)

        Logger.info(f"BuyTicketInfo PurchaseInfo={serializer.validated_data} User={self.request.user}")


class PurchaseDetailsAPIView(RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Transaction.objects.all()
    lookup_field = "id"
    permission_classes = [IsOwnerOrAdmin]


class GatewayCallbackAPIView(APIView):
    """
    as the user pays successfully the gateway hook will call this api,
    many security stuff like gateway auth_token are not implemented here.
    """
    permission_classes = [AllowAny]  # This is WRONG and MUST authenticate the BANK!!!!

    def post(self, request, *args, **kwargs):
        data = request.data
        payment_status = data.get("status", "")

        transaction_id = data.get("transaction_id", "")
        ticket_id = data.get("ticket_id", "")
        user_id = data.get("user_id", "")

        if not transaction_id:
            Logger.warning(f"BankGateway Callback [NO TransactionID] TransactionInfo={data}")
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            transaction = Transaction.objects.get(id=transaction_id)
        except Transaction.DoesNotExist:
            Logger.warning(f"BankGateway Callback [Transaction 404] TransactionInfo={data}")
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not all([ticket_id, user_id]):
            transaction.set_failed()
            Logger.warning(f"BankGateway Callback [Incorrect DATA] TransactionInfo={data}")
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            transaction.set_failed()
            Logger.warning(f"BankGateway Callback [User 404] TransactionInfo={data}")
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            transaction.set_failed()
            Logger.warning(f"BankGateway Callback [Ticket 404] TransactionInfo={data}")
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not payment_status.strip().lower() == "success":
            transaction.set_failed()
            Logger.warning(f"BankGateway Callback [FAILED Transaction] TransactionInfo={data}")
            return Response()

        transaction.set_succeed()
        ticket.set_owner(user.id)
        return Response()
