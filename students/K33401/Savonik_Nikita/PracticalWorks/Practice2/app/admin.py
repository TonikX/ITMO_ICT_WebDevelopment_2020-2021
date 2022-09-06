from django.contrib import admin
from .models import *


admin.site.register(Car)
admin.site.register(Car_owner)
admin.site.register(Driving_license)
admin.site.register(Ownership)
admin.site.register(Owner_info)

