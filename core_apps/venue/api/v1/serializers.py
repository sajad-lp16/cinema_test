from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core_apps.venue.models import (
    Stadium,
    Seat,
    Match
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
            "title",
            "stadium",
            "vip_price",
            "normal_price",
            "start_time",
            "end_time",
        )
