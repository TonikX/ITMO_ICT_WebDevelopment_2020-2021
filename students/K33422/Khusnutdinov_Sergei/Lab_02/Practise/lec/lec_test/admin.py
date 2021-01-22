from django.contrib import admin
from .models import Publisher, Book

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Book)