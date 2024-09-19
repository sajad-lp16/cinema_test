from django.dispatch import receiver
from django.db.models.signals import post_save

from core_apps.venue.models import (
    Stadium,
    Seat
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
