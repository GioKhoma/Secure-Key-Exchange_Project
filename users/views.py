from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status
from .serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)


# for session auth
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return Response({'message': 'Login Successful'}, status=status.HTTP_200_OK)
#
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
