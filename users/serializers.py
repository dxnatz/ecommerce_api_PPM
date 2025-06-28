from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio', 'is_banned', 'is_moderator']
        read_only_fields = ['id', 'is_banned', 'is_moderator']

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user