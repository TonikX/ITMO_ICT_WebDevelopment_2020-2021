from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Review)
admin.site.register(Booking)