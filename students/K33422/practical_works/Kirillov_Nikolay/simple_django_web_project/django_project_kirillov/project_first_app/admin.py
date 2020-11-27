from django.contrib import admin
from .models import Driver, DriverLicence, Car, Ownership

admin.site.register(Driver)
admin.site.register(DriverLicence)
admin.site.register(Car)
admin.site.register(Ownership)
