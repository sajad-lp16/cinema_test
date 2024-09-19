from django.db.models import Manager

from core_apps.common.managers import IsActiveManager
from core_apps.venue.cache import TicketCache


class StadiumManager(IsActiveManager):
    """Custom manager for Stadium model."""


class SeatManager(IsActiveManager):
    """Custom manager for Seat model."""

    def get_vip_seats(self):
        return super().get_queryset().filter(is_vip=True)

    def get_normal_seats(self):
        return super().get_queryset().filter(is_vip=False)


class MatchManager(IsActiveManager):
    """Custom manager for Match model."""


class TicketManager(Manager):
    """Custom manager for ticket model."""
    _cache_manager = TicketCache

    def get_available_tickets(self, match_id: int = None):
        locked_ticket_ids = self._cache_manager.get_locked_tickets_ids()
        queryset = super().get_queryset().exclude(id__in=locked_ticket_ids).filter(
            status__in=self.model.sell_ok_options()
        )
        if match_id is None:
            return queryset
        return queryset.filter(match_id=match_id)
