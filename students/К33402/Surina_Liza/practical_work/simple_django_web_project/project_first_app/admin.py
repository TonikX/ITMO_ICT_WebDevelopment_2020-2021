from django.contrib import admin
from .models import CarOwner, Owner, Car, Card, ExampleModel


admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Card)
admin.site.register(Owner)
admin.site.register(ExampleModel)
