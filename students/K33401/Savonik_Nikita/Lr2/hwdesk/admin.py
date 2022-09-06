from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
            'username',
            'type',
            'first_name',
            'last_name',
        ]

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Teacher)
admin.site.register(Pupil)
admin.site.register(Task)
admin.site.register(LoadTask)
admin.site.register(CheckTask)
