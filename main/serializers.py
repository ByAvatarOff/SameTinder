from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, AddContent, Like, Chat


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения юзера"""
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения профилей юзеров"""
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'image', 'name', 'surname', 'group', 'geo_location']


class CreateProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для создания профиля юзера"""
    class Meta:
        model = Profile
        fields = '__all__'


class UpdateProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для создания профиля юзера"""
    class Meta:
        model = Profile
        exclude = ['user', ]


class UpdateLocationProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['geo_location']


class AddContentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = AddContent
        fields = '__all__'


class CreateAddContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddContent
        fields = ['image', 'description']


class CreateLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['profile', 'like']


class CreateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ['message', 'sub_chat', ]


class ListMessageSerializer(serializers.ModelSerializer):
    owner_chat = UserSerializer()
    sub_chat = UserSerializer()

    class Meta:
        model = Chat
        fields = '__all__'
