from django.contrib import admin
from .models import User, Conf, Review, Reserve
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Conf)
admin.site.register(Review)
admin.site.register(Reserve)