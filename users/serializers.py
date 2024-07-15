from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

