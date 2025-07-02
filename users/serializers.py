from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio', 'is_banned', 'is_active']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            user_obj = CustomUser.objects.filter(username=username).first()
            if user_obj:
                if user_obj.is_banned:
                    raise AuthenticationFailed("Utente bannato, impossibile fare il login")
                else:
                    raise AuthenticationFailed("Credenziali non valide")
            else:
                raise AuthenticationFailed("Credenziali non valide")

        if user.is_banned:
            raise AuthenticationFailed("Utente bannato, impossibile fare il login")

        self.user = user
        return super().validate(attrs)