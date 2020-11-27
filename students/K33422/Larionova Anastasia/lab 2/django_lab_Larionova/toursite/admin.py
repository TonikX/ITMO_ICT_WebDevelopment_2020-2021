from django.contrib import admin
from .models import User, Tour, Review, Reserve
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Tour)
admin.site.register(Review)
admin.site.register(Reserve)