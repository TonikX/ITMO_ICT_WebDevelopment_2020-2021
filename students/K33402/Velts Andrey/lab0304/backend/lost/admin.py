from django.contrib import admin
from .models import Lost


@admin.register(Lost)
class LostAdmin(admin.ModelAdmin):
    pass
