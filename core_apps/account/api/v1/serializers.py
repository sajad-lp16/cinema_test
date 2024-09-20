from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "password",
            "password_repeat",
            "mobile",
        )

    def validate_password(self, value):
        repeat = self.initial_data.get("password_repeat")
        if value != repeat:
            raise serializers.ValidationError("Passwords do not match.")
        validate_password(value)
        return value

    def create(self, validated_data):
        validated_data.pop("password_repeat")
        try:
            user = User.objects.create_user(**validated_data)
        except ValidationError:
            raise serializers.ValidationError({"mobile": "User this mobile already exists."})
        return user


class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
