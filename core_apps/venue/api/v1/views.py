from rest_framework import generics
from rest_framework.permissions import AllowAny

from core_apps.venue.api.v1.permissions import IsAdminUserOrReadOnly
from core_apps.venue.models import (
    Stadium,
    Match,
    Ticket
)
from core_apps.venue.api.v1.pagination import (
    StadiumPagination,
    MatchPagination,
    TicketPagination
)
from core_apps.venue.api.v1.serializers import (
    StadiumSerializer,
    MatchSerializer,
    TicketSerializer
)


class StadiumListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StadiumSerializer
    pagination_class = StadiumPagination
    queryset = Stadium.enable_objects.all()
    permission_classes = [IsAdminUserOrReadOnly]


class StadiumDetailAPIView(generics.RetrieveAPIView):
    serializer_class = StadiumSerializer
    queryset = Stadium.enable_objects.all()
    lookup_field = "id"
    permission_classes = [AllowAny]


class MatchListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MatchSerializer
    pagination_class = MatchPagination
    queryset = Match.enable_objects.all()
    permission_classes = [IsAdminUserOrReadOnly]


class MatchDetailAPIView(generics.RetrieveAPIView):
    serializer_class = MatchSerializer
    queryset = Match.enable_objects.all()
    lookup_field = "id"
    permission_classes = [AllowAny]


class TicketList(generics.ListAPIView):
    queryset = Ticket.enable_objects.get_available_tickets()
    serializer_class = TicketSerializer
    pagination_class = TicketPagination
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        match_id = self.kwargs["match_id"]
        return Ticket.enable_objects.get_available_tickets(match_id=match_id)
