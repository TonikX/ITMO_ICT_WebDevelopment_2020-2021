from django.contrib import admin
from .models import Hotel, Room, Reserve, Feedback

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reserve)
admin.site.register(Feedback)