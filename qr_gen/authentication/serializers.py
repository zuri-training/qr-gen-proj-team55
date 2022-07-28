from click import password_option
from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=25, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password",
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = password = serializers.CharField(
        max_length=25, min_length=6, write_only=True
    )

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "token",
        )

        read_only_fields = ["token"]
