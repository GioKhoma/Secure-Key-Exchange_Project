from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Channel
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ChannelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

User = get_user_model()


class ChannelViewSet(ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender_user=self.request.user)

    # def get_queryset(self):
    #     return User.objects.exclude(id=self.request.user.id)


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BaseAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)
