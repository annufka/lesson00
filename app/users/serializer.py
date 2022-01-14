from django.contrib.auth.models import User
from rest_framework import serializers

from app.users.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True, many=False)
    photo = serializers.ImageField()
    class Meta:
        model = Profile
        fields = '__all__'