from drf_yasg import openapi

LOGIN_API_SCHEMA = {
    200: openapi.Response(
        description="Login successful",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "access": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Access token should be used with `token` prefix",
                    pattern="ey ...",
                ),
                "refresh": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Refresh token",
                    pattern="ey ...",
                ),
            }
        )
    )
}

REGISTER_API_SCHEMA = {
    201: openapi.Response(
        description="Register successful",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "access": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Access token should be used with `token` prefix",
                    pattern="ey ...",
                ),
                "refresh": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Refresh token",
                    pattern="ey ...",
                ),
            }
        )
    )
}

