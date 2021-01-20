from django.contrib import admin
from .models import Car, Owner, Ownership, DrivingLicense

# Register your models here.
admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(DrivingLicense)
