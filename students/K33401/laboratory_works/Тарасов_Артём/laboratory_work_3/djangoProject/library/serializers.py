from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.author = validated_data.get('author', instance.author)
        instance.name = validated_data.get('name', instance.name)
        instance.year_of_pub = validated_data.get('year_of_pub', instance.year_of_pub)
        instance.section = validated_data.get('section', instance.section)
        instance.pressmark = validated_data.get('pressmark', instance.pressmark)
        instance.debit_date = validated_data.get('debit_date', instance.debit_date)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = "__all__"


class ReaderSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Reader.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.passport_number = validated_data.get('passport_number', instance.passport_number)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.graduate_degree = validated_data.get('graduate_degree', instance.graduate_degree)
        instance.books = validated_data.get('graduate_degree', instance.books)
        instance.save()
        return instance

    class Meta:
        model = Reader
        fields = "__all__"


class InstanceOfBookSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return InstanceOfBook.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.id_book = validated_data.get('id_book', instance.id_book)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        model = InstanceOfBook
        fields = "__all__"


class IssuingAInstanceSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return IssuingAInstance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.instance = validated_data.get('instance', instance.instance)
        instance.reader = validated_data.get('reader', instance.reader)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.return_date = validated_data.get('return_date', instance.return_date)
        instance.save()
        return instance

    class Meta:
        model = IssuingAInstance
        fields = "__all__"


class ReadingRoomSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ReadingRoom.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.save()
        return instance

    class Meta:
        model = ReadingRoom
        fields = "__all__"


class InstanceOfBookInReadingRoomSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return InstanceOfBookInReadingRoom.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_instance = validated_data.get('id_instance', instance.id_instance)
        instance.id_room = validated_data.get('id_room', instance.id_room)
        instance.count = validated_data.get('count', instance.count)
        instance.save()
        return instance

    class Meta:
        model = InstanceOfBookInReadingRoom
        fields = "__all__"


class RegistersSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Registers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_reader = validated_data.get('id_reader', instance.id_reader)
        instance.id_room = validated_data.get('id_room', instance.id_room)
        instance.register_date = validated_data.get('register_date', instance.register_date)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.unregister_date = validated_data.get('unregister_date', instance.unregister_date)
        instance.save()
        return instance

    class Meta:
        model = Registers
        fields = "__all__"
