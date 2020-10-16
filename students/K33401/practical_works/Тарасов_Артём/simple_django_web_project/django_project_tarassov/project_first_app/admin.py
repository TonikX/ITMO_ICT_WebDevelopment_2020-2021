from django.contrib import admin
from .models import Car, Driver, DrivingLicence, Owning

admin.site.register(Car)
admin.site.register(DrivingLicence)
admin.site.register(Driver)
admin.site.register(Owning)
