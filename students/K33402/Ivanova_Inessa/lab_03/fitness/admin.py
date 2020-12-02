from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Coach)
admin.site.register(Client)
admin.site.register(Session)
admin.site.register(Booking)
admin.site.register(Lesson)