from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from racing_scoreboard.models import *

admin.site.register(User, UserAdmin)
admin.site.register(Race)
admin.site.register(RaceRacer)
admin.site.register(Racer)
admin.site.register(Comment)
