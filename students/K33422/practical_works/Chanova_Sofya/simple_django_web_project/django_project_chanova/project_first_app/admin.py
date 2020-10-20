from django.contrib import admin
from .models import Owner, Car, CarOwnership, DriverLicense

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(CarOwnership)
admin.site.register(DriverLicense)
