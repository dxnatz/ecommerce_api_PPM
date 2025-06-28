from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio' , 'is_banned', 'is_moderator']
        read_only_fields = ['id', 'username', 'is_banned', 'is_moderator']