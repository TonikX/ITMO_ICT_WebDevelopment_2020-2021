from django.contrib import admin

# Register your models here.
from .models import Owner, Ownership, Auto, Driver_licence
admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(Auto)
admin.site.register(Driver_licence)
