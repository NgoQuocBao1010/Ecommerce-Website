from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        exclude = ('user', 'id', 'dateCreated')
    
    def get_email(self, obj):
        return obj.user.email