from rest_framework.serializers import ModelSerializer

from core_apps.venue.models import (
    Stadium,
    Seat,
    Match,
    Ticket
)


class StadiumSerializer(ModelSerializer):
    class Meta:
        model = Stadium
        fields = (
            "id",
            "title",
            "vip_seats",
            "normal_seats",
        )


class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = (
            "stadium",
            "number",
            "is_vip"
        )


class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "id",
            "title",
            "stadium",
            "start_time",
            "end_time",
        )


class TicketSerializer(ModelSerializer):
    match = MatchSerializer()

    class Meta:
        model = Ticket
        fields = (
            "id",
            "price",
            "match",
            "seat",
            "is_vip"
        )
