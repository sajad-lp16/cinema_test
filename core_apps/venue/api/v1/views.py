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


class TicketList(generics.ListAPIView):
    queryset = Ticket.enable_objects.get_available_tickets()
    serializer_class = TicketSerializer
    pagination_class = TicketPagination
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        match_id = self.kwargs["match_id"]
        return Ticket.enable_objects.get_available_tickets(match_id=match_id)
