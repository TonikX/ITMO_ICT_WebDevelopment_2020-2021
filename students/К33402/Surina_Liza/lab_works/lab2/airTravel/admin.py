from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import admin

admin.site.register(Schedule)
admin.site.register(Booking)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'created')


admin.site.register(Comments, CommentAdmin)
