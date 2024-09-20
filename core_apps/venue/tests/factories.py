from factory.django import DjangoModelFactory

from core_apps.venue.models import (
    Stadium,
    Match,
    Seat,
    Ticket
)


class StadiumFactory(DjangoModelFactory):
    """transaction model factory for testsing"""

    class Meta:
        model = Stadium


class MatchFactory(DjangoModelFactory):
    """transaction model factory for testsing"""

    class Meta:
        model = Match


class SeatFactory(DjangoModelFactory):
    """transaction model factory for testsing"""

    class Meta:
        model = Seat


class TicketFactory(DjangoModelFactory):
    """transaction model factory for testsing"""

    class Meta:
        model = Ticket
