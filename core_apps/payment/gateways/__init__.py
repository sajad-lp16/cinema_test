from core_apps.payment.gateways.base import BasePaymentGateway

from core_apps.payment.gateways.imaginary_gateway import ImaginaryGateway

# This mapping has to be handled dynamically! ex: django-constance
GATEWAYS_MAPPING = {
    "imaginary": ImaginaryGateway,
}


def get_gateway_by_name(name: str) -> BasePaymentGateway:
    name = name.strip().lower()
    gateway = GATEWAYS_MAPPING.get(name)
    assert gateway is not None, "Invalid gateway name"

    return gateway()


def get_all_gateways_name() -> list[str]:
    return list(GATEWAYS_MAPPING.keys())
