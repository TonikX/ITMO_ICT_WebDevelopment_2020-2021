from django.contrib import admin
from .models import Driver, DriverDocument, Possession, Car, User

# Register your models here.

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(DriverDocument)
admin.site.register(Possession)
admin.site.register(Car)
