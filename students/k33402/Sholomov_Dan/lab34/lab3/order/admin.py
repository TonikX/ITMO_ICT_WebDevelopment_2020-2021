from django.contrib import admin
from .models import Order, OrderedItem


@admin.register(Order)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderedItem)
class ItemAdmin(admin.ModelAdmin):
    pass
