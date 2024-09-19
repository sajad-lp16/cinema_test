from abc import ABC, abstractmethod


class BasePaymentGateway(ABC):
    """
    Base class for Payment Gateways.
    This class usually has more necessary methods, here one is writen for test scenario.
    """

    __CLS_2_INSTANCE_MAPPING = {}

    def __new__(cls, *args, **kwargs):
        """
        Singleton behavior avoids multiple instantiation,
        This implementation supports multiple gateways.
        """
        assert cls is not BasePaymentGateway, "BasePaymentGateway is abstract"

        instance = cls.__CLS_2_INSTANCE_MAPPING.get(cls)
        if instance is None:
            instance = super().__new__(cls)
            cls.__CLS_2_INSTANCE_MAPPING[cls] = instance

        return instance

    @abstractmethod
    def perform_payment(self, price: int, payload: dict) -> bool:
        pass
