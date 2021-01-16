from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username", "first_name", "last_name", "email"


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username",


class CreationFullSerializer(serializers.ModelSerializer):
    creator = AuthorSerializer()

    class Meta:
        model = Creation
        fields = "__all__"


class CreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creation
        fields = "__all__"


class ReviewFullSerializer(serializers.ModelSerializer):
    author = UserSerializer(default=serializers.CurrentUserDefault())
    creation = CreationSerializer()

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    author = UserNameSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = "__all__"
