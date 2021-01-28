from django.contrib import admin
from .models import Person
from .models import Car
from .models import DriverLicence
from .models import Ownership

admin.site.register(Person)
admin.site.register(Car)
admin.site.register(DriverLicence)
admin.site.register(Ownership)