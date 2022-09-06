from django.contrib import admin
from .models import Driver, Car, Documents, Ownership
from django.contrib.auth.admin import UserAdmin

admin.site.register(Driver, UserAdmin)
admin.site.register(Car)
admin.site.register(Documents)
admin.site.register(Ownership)

