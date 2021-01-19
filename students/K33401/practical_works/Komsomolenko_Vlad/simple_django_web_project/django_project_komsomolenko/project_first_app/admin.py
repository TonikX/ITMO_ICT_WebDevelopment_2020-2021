from django.contrib import admin
from .models import Owner
from .models import Car
from .models import Possession
from .models import License
from .models import User

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Possession)
admin.site.register(License)
admin.site.register(User)