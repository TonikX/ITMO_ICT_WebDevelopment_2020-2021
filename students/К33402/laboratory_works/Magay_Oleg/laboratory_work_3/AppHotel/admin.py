from django.contrib import admin
from .models import *

admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Staff)
admin.site.register(StaffCleaning)
admin.site.register(CleaningParams)