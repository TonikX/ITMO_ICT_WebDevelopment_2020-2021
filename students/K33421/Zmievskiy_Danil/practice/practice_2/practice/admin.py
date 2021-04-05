from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(DriverLicense)
admin.site.register(Ownership)
