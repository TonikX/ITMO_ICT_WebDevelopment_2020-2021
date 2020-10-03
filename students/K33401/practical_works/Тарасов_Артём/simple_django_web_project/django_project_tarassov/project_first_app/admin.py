from django.contrib import admin
from .models import Driver, DriverDocument, Possession, Car


admin.site.register(Driver)
admin.site.register(DriverDocument)
admin.site.register(Possession)
admin.site.register(Car)
