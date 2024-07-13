from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Channel
from rest_framework.permissions import IsAuthenticated
from .serializers import ChannelSerializer
import uuid


class ChannelViewSet(ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender_user=self.request.user)

