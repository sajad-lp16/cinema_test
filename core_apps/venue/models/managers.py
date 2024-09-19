from core_apps.common.managers import IsActiveManager


class StadiumManager(IsActiveManager):
    """Custom manager for the Stadium model."""


class SeatManager(IsActiveManager):
    """Custom manager for the Seat model."""


class MatchManager(IsActiveManager):
    """Custom manager for the Match model."""
