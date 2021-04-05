from django.contrib import admin
from hotels_app.models import *

admin.site.register(Client)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(Review)
admin.site.register(Reservation)

