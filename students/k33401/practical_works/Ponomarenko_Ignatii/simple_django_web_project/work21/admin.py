from django.contrib import admin
from .models import CarOwner, Car, Ownership, License

# Register your models here.

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(License)