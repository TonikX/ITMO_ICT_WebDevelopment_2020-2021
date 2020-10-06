from django.contrib import admin
from .models import Owner
from .models import Car
from .models import Possession
from .models import License

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Possession)
admin.site.register(License)