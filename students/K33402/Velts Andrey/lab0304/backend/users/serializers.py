from django.contrib.auth import authenticate, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import ugettext_lazy as _
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from home.serializers import ThumbnailSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    image = ThumbnailSerializer("avatar", "image")
    location = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "image",
            "first_name",
            "last_name",
            "name",
            "email",
            "city",
            "country",
            "location",
            "phone_number",
        )
        read_only_fields = [
            "date_joined",
            "is_staff",
        ]
        extra_kwargs = {
            "email": {"required": False},
            "username": {"required": False},
        }

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_location(self, obj):
        return f"{obj.city}, {obj.country}" if obj.city else obj.country


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("image",)


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password1": {"required": True, "write_only": True},
            "password2": {"required": True, "write_only": True},
            "password": {"required": False},
            "username": {"required": False},
            "email": {"required": True},
            "phone_number": {"required": False},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, data):
        username = data.get("email").split("@")[0].lower()
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            raise serializers.ValidationError(
                _("Пользователь с данным логином уже зарегистрирован.")
            )
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError(_("Пароли не совпадают."))
        return data

    def create(self, validated_data):
        data = validated_data
        username = data.get("email").split("@")[0]
        email = data.get("email")
        password = data.get("password1")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        country = data.get("country")
        country_code = data.get("country_code")
        city = data.get("city")
        phone_number = data.get("phone_number")
        user = User.objects.create_user(
            username,
            email,
            password,
            first_name=first_name,
            last_name=last_name,
            country=country,
            country_code=country_code,
            city=city,
            phone_number=phone_number,
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Вы ввели невереные данные")


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """

    email = serializers.EmailField()

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        try:
            email = validated_data.get("email", "")
            self.user = User.objects.get(email=email)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            raise ValidationError({"email": "Пользователь с данным email не найден."})
        return validated_data


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """

    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()

    set_password_form_class = SetPasswordForm

    default_error_messages = {
        "invalid_token": _("Недействителен ключ подтверждения."),
        "invalid_uid": _("Пользователь не найден."),
    }

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        # Decode the uidb64 to uid to get User object
        try:
            uid = urlsafe_base64_decode(validated_data.get("uid", ""))
            self.user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            key_error = "invalid_uid"
            raise ValidationError(
                {"error": self.error_messages[key_error]}, code=key_error
            )

        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(self.user, attrs["token"]):
            key_error = "invalid_token"
            raise ValidationError(
                {"error": self.error_messages[key_error]}, code=key_error
            )

        return attrs

    def save(self):
        return self.set_password_form.save()


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")
        self.user = getattr(self.request, "user", None)

    def validate_old_password(self, value):
        if self.user and not self.user.check_password(value):
            err_msg = "Пароль не изменён, так как прежний пароль введён неправильно."
            raise serializers.ValidationError(err_msg)
        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(
                "Пароль не изменён, так как новый пароль повторен неправильно"
            )
        return attrs

    def save(self):
        self.set_password_form.save()
        update_session_auth_hash(self.request, self.user)
