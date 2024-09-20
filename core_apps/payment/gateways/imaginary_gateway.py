from core_apps.payment.gateways.base import BasePaymentGateway


class ImaginaryGateway(BasePaymentGateway):
    """better to be a model containing Logo etc... . ( simplified:) )"""

    def perform_payment(self, price: int, payload: dict, callback: str) -> bool:
        """Suppose all payments are succeeded"""
        return True
