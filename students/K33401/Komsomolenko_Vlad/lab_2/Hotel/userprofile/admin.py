from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from accounts.forms import SignUpForm, CustomUserChangeForm


# Определяем новый класс настроек для модели User
class CustomUserAdmin(UserAdmin):
    model = UserProfile
    add_form = SignUpForm
    form = CustomUserChangeForm
    list_display = [
        'username', 'first_name', 'last_name', 'type',
    ]


# Перерегистрируем модель User
admin.site.register(UserProfile, CustomUserAdmin)