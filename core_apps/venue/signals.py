from django.dispatch import receiver
from django.db.models.signals import post_save

from core_apps.venue.models import (
    Stadium,
    Seat,
    Match,
    Ticket
)


@receiver(post_save, sender=Stadium)
def create_seats_for_stadium(sender, instance: Stadium, created: bool, **kwargs):
    if created:
        normal_counter_start = 1
        normal_counter_end = instance.normal_seats + 1

        vip_counter_start = normal_counter_end
        vip_counter_end = vip_counter_start + instance.vip_seats

        normal_seats = [
            Seat(stadium=instance, number=counter) for counter in range(normal_counter_start, normal_counter_end)
        ]
        vip_seats = [
            Seat(stadium=instance, number=counter, is_vip=True) for counter in range(vip_counter_start, vip_counter_end)
        ]
        Seat.objects.bulk_create(normal_seats + vip_seats)


@receiver(post_save, sender=Match)
def generate_tickets_for_match(sender, instance: Match, created: bool, **kwargs):
    """creates tickets for `is_active` seats for specified for a match"""
    if created:
        vip_seats = Seat.enable_objects.get_vip_seats().filter(
            stadium_id=instance.stadium_id
        )
        normal_seats = Seat.enable_objects.get_normal_seats().filter(
            stadium_id=instance.stadium_id
        )

        vip_tickets = [
            Ticket(is_vip=True, price=instance.vip_price, match=instance, seat=seat) for seat in vip_seats
        ]

        normal_tickets = [
            Ticket(price=instance.normal_price, match=instance, seat=seat) for seat in normal_seats
        ]

        Ticket.objects.bulk_create(vip_tickets + normal_tickets)


@receiver(post_save, sender=Match)
def revoke_tickets(sender, instance: Match, created: bool, **kwargs):
    """revoke all match tickets if match is canceled"""
    if not created and not instance.is_active:
        instance.tickets.update(
            status=Ticket.StatusOptions.REVOKED
        )
    # Should Refund the tickets price to the user :)
