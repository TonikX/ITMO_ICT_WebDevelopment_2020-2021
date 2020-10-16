from django.contrib import admin

from .models import *

admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DrivingLicence)