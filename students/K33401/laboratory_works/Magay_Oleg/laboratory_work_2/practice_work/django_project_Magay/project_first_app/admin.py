from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(Ownership)
admin.site.register(User)