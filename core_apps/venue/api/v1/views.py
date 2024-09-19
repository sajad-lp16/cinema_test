from rest_framework import generics
from rest_framework.permissions import AllowAny

from core_apps.venue.api.v1.permissions import IsAdminUserOrReadOnly
from core_apps.venue.models import (
    Stadium,
    Match
)
from core_apps.venue.api.v1.pagination import (
    StadiumPagination,
    MatchPagination
)
from core_apps.venue.api.v1.serializers import (
    StadiumSerializer,
    MatchSerializer
)


class StadiumListCreateAPIView(generics.ListCreateAPIView):
    pagination_class = StadiumPagination
    queryset = Stadium.enable_objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = StadiumSerializer


class StadiumDetailAPIView(generics.RetrieveAPIView):
    queryset = Stadium.enable_objects.all()
    lookup_field = "id"
    permission_classes = [AllowAny]
    serializer_class = StadiumSerializer


class MatchListCreateAPIView(generics.ListCreateAPIView):
    pagination_class = MatchPagination
    queryset = Match.enable_objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = MatchSerializer


class MatchDetailAPIView(generics.RetrieveAPIView):
    queryset = Match.enable_objects.all()
    lookup_field = "id"
    permission_classes = [AllowAny]
    serializer_class = MatchSerializer
