from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import CustomUser
from users.permissions import IsModeratore
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer

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
    permission_classes = [IsAuthenticated, IsModeratore]

    def perform_update(self, serializer):
        serializer.save(is_banned=True, is_active=False)

class UserMeAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsModeratore]

    def get_object(self):
        return self.request.user

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsModeratore]

    def perform_destroy(self, instance):
        if self.request.user == instance:
            raise PermissionDenied("Non puoi eliminare te stesso.")
        instance.delete()

class UserUnbanAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsModeratore]

    def patch(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        if not user.is_banned:
            return Response({"detail": "Utente non è bannato."}, status=status.HTTP_400_BAD_REQUEST)

        user.is_banned = False
        user.is_active = True
        user.save()
        return Response({"detail": f"L'utente {user.username} è stato sbannato."}, status=status.HTTP_200_OK)

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer