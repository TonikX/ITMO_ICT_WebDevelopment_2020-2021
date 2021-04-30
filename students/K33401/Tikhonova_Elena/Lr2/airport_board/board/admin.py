from django.contrib import admin
from .models import Flight, User, Reservation

admin.site.register(Flight)
admin.site.register(User)
admin.site.register(Reservation)
