from django.urls import path

from core_apps.venue.api.v1.views import (
    StadiumListCreateAPIView,
    StadiumDetailAPIView,
    MatchListCreateAPIView,
    MatchDetailAPIView
)

app_name = "v1"

urlpatterns = [
    path("stadium/", StadiumListCreateAPIView.as_view(), name="stadium_list_create"),
    path("stadium/<int:id>/", StadiumDetailAPIView.as_view(), name="stadium_detail"),

    path("match/", MatchListCreateAPIView.as_view(), name="match_list_create"),
    path("match/<int:id>", MatchDetailAPIView.as_view(), name="match_detail"),
]
