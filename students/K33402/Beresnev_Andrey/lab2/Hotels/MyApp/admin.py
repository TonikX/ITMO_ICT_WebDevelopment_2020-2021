from django.contrib import admin
from .models import Room, Hotel, Client, ReservedRooms, Review

admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(Client)
admin.site.register(ReservedRooms)
admin.site.register(Review)
