from django.contrib import admin
from .models import *
from .forms import TeacherCreationForm, StudentCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = TeacherCreationForm
    list_display = [
            'username',
            'role',
            'subject',
            'name',
            'group_number',
        ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Homework)
admin.site.register(Assignment)
admin.site.register(Assessment)
