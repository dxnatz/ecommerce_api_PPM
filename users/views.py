from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView

from users.models import CustomUser
from users.permissions import IsModerator
from users.serializers import UserSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })

class UserBanAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsModerator]

    def perform_update(self, serializer):
        serializer.save(is_banned=True)

class UserMeAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsModerator]

    def perform_destroy(self, instance):
        if self.request.user == instance:
            raise PermissionDenied("Non puoi eliminare te stesso.")
        instance.delete()

class UserUnbanAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsModerator]

    def patch(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        if not user.is_banned:
            return Response({"detail": "Utente non è bannato."}, status=status.HTTP_400_BAD_REQUEST)

        user.is_banned = False
        user.save()
        return Response({"detail": f"L'utente {user.username} è stato sbannato."}, status=status.HTTP_200_OK)

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]