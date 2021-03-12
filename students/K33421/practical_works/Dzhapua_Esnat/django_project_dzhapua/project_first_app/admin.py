from django.contrib import admin
from .models import Carowner, License, Car, Ownership

# Register your models here.

admin.site.register(Carowner)
admin.site.register(License)
admin.site.register(Car)
admin.site.register(Ownership)