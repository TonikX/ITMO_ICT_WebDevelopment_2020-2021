from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Flight)
admin.site.register(Place)
admin.site.register(Comment)
admin.site.register(Airline)
admin.site.register(CityAirport)
