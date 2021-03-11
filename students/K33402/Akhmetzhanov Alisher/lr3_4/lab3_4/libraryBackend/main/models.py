from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

import datetime


from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_librarian = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_librarian']
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Reader(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='reader_profile')
    reader_ticket = models.IntegerField(default=100)
    passport = models.CharField(max_length=300)
    birth_date = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=210, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    is_scientist = models.BooleanField(default=False)
    hall = models.ForeignKey('LibraryHall', on_delete=models.CASCADE, related_name="readers", blank=True, null=True)

    def __str__(self) -> str:
        return self.user.email


class Librarian(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='librarian_profile')
    experience = models.CharField(max_length=250, default="Опыт есть")

    def __str__(self) -> str:
        return self.user.email + " -> " + self.experience


class Book(models.Model):
    title = models.CharField(max_length=210)
    author = models.CharField(max_length=410)
    realise_date = models.DateField(default=datetime.date.today)
    publishing_house = models.CharField(max_length=210)

    def __str__(self) -> str:
        return self.title + ' ' +  self.author


class LibraryHall(models.Model):
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=210)
    capacity = models.IntegerField(default=10)

    def __str__(self) -> str:
        return str(self.number) + ' ' + self.title


class BookReplica(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_copies')
    cipher = models.IntegerField(default=1)
    library_hall = models.ForeignKey(LibraryHall, on_delete=models.CASCADE, related_name='hall_copies')
    current_reader = models.ForeignKey(Reader, on_delete=models.CASCADE, blank=True, null=True, related_name='reading_books')

    def __str__(self) -> str:
        return self.library_hall.title + ' -> ' + self.book.title

