from rest_framework import serializers
from .models import Channel
from users.models import CustomUser


class ChannelSerializer(serializers.ModelSerializer):
    sender_user = serializers.CharField(source='sender_user.email', read_only=True)
    class Meta:
        model = Channel
        fields = ['sender_user', 'recipient_user', 'name']


class ChannelSenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'sender_user']


class ChannelRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'recipient_user']
