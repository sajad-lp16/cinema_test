from django.contrib.auth import get_user_model

from factory.django import DjangoModelFactory

User = get_user_model()


class UserFactory(DjangoModelFactory):
    """
    User model factory for testing.
    """

    class Meta:
        model = User
