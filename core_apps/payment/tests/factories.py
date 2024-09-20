from factory.django import DjangoModelFactory

from core_apps.payment.models import Transaction


class TransactionFactory(DjangoModelFactory):
    """transaction model factory for testsing"""
    class Meta:
        model = Transaction
