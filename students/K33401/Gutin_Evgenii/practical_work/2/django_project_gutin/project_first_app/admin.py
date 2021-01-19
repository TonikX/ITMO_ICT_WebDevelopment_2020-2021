from .models import *
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(DriverLicense)
class DriverLicenseAdmin(admin.ModelAdmin):
    pass


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass
