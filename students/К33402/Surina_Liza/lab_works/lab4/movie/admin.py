from django.contrib import admin
from .models import Client, Movie, Review

admin.site.register(Client)
admin.site.register(Movie)


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Review
    extra = 1
    readonly_fields = ("name", "email")
