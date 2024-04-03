
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

from .models import Profile

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','first_name','last_name','username','email','password']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
