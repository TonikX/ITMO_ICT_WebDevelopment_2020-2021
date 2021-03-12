from django.contrib import admin
from .models import User, Tour, Comment, Reservation
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Tour)
admin.site.register(Comment)
admin.site.register(Reservation)
