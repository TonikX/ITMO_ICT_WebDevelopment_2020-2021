from django.contrib import admin
from .models import Driver, Car, DriverLicense, Ownership


admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriverLicense)