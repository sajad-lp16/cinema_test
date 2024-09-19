from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView
)

from core_apps.venue.models import Ticket
from core_apps.payment.api.v1.permissions import IsOwnerOrAdmin
from core_apps.payment.models import Transaction
from core_apps.payment.api.v1.serializers import PaymentSerializer
from core_apps.payment.gateways import get_all_gateways_name


class GatewaysListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        response = {"gateways": get_all_gateways_name()}
        return Response(response, status=status.HTTP_200_OK)


class BuyTicketAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Transaction.objects.all()


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

    def post(self, request, *args, **kwargs):
        pass
