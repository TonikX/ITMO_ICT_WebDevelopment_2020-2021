from django.contrib import admin

from .models import User, Car, Certification, Possession

# Register your models here.

@admin.register(User)
class UserRegister(admin.ModelAdmin):
    pass

admin.site.register(Car)
admin.site.register(Certification)
admin.site.register(Possession)

