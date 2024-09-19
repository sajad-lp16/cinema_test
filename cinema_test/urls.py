from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    path,
    include
)

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="EBT Server API",
        default_version="v1",
        description="API For The Project",
        contact=openapi.Contact(email="sajad.tohidi76@gmail.com"),
        license=openapi.License("MIT License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("account/", include("core_apps.account.urls", namespace="account")),
    path("venue/", include("core_apps.venue.urls", namespace="venue")),
    path("payment/", include("core_apps.payment.urls", namespace="payment")),
]

if settings.DEBUG:
    urlpatterns += [
        path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
        path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ]

admin.site.site_header = "EBT Server API Admin"
admin.site.site_title = "EBT ServerAPI Admin Portal"
admin.site.index_title = "Welcome to EBT Server"
