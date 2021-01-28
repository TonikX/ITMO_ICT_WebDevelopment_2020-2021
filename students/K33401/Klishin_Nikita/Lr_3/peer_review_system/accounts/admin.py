from django import forms
from django.contrib import admin
from django.contrib.admin.sites import site
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (
	CustomUser,
	StudentProfile, TeacherProfile
)

from django.contrib.auth.models import Group


class CustomUserAdmin(BaseUserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	# model = CustomUser
	
	list_display = ['email', 'admin', 'is_teacher']
	list_filter = ('admin',)

	fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'surname', 'birth_date')}),
        ('Status', {'fields': ('is_teacher',)}),
		('Permissions', {'fields': ('admin',)}),
    )

	add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'surname', 'birth_date')}),
        ('Status', {'fields': ('is_teacher',)}),
	)

	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()


class StudentProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'student_class']


class TeacherProfileAdmin(admin.ModelAdmin):
	list_display = ['user']

admin.site.register(CustomUser, CustomUserAdmin)
admin,site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)

admin.site.unregister(Group)
