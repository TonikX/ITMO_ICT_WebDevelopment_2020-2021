from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Driver)
admin.site.register(models.Route)
admin.site.register(models.Bus)
admin.site.register(models.Shift)
