from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver, Car, Docs, Ownership

# Register your models here.

admin.site.register(Driver, UserAdmin)
admin.site.register(Car)
admin.site.register(Docs)
admin.site.register(Ownership)