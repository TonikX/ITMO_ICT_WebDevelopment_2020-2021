from django.contrib import admin

from .models import Owner
from .models import Car
from .models import Possession
from .models import Licence
# Register your models here.
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Possession)
admin.site.register(Licence)