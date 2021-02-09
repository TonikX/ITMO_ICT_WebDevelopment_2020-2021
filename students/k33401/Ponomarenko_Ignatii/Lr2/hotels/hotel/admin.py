from django.contrib import admin
from .models import Guest, Hotel, RoomType, Booking, Review


# Register your models here.
admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(Booking)
admin.site.register(Review)