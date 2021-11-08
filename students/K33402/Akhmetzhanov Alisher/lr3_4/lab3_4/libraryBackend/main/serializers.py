from django.db.models import fields, query
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from .models import *

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_librarian']
        ref_name = "Custom user"


class UserRegistrationSerializer(UserCreateSerializer):

    def create(self, validated_data):
        print("Register")
        createdUser = super().create(validated_data)
        
        if not validated_data['is_librarian']:
            Reader.objects.create(
                user = createdUser,
                passport = "123456789",
                phone = "+71231231212",
                is_scientist = False,
            )
        else:
            Librarian.objects.create(
                user = createdUser
            )
        return createdUser

    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'password', 'is_librarian')


class ReaderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = UserSerializer(instance=instance.user).data
        return data
    
    def validate(self, data):
        print("ReaderSerializer -> Validation:", self.instance)
        if (data['hall'] == None and self.instance.reading_books.filter(library_hall=self.instance.hall).exists()):
            raise serializers.ValidationError("У вас присутствуют не сданые книги. Пожалуйста, сдайте их")
        return super().validate(data)

    class Meta:
        model = Reader
        fields = ('id', 'user', 'reader_ticket', 'passport', 'birth_date', 'address', 'phone', 'is_scientist', 'hall')


class LibrarianSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Librarian
        fields = ('user', 'experience', )


class LibraryHallSerializer(serializers.ModelSerializer):
    readers = serializers.PrimaryKeyRelatedField(many=True, queryset=Reader.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['readers'] = ReaderSerializer(instance=instance.readers.all(), many=True).data
        return data

    class Meta:
        model = LibraryHall
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class BookReplicaSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['book'] = BookSerializer(instance=instance.book).data
        return data

    class Meta:
        model = BookReplica
        fields = "__all__"




