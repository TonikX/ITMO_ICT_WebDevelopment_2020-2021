from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20, blank=True, null=True, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{} {} {} {}".format(self.username, self.name, self.email, self.date_of_birth)


class Review(models.Model):
    RATING = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    creation = models.ForeignKey("Creation", on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    rating = models.IntegerField(choices=RATING)


class Creation(models.Model):
    TYPE = [('Изобразительное искусство', 'Изобразительное искусство'), ('Кино', 'Кино'), ('Литература', 'Литература'),
            ('Музыка', 'Музыка')]
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    creator = models.ForeignKey("Author", null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=25,choices=TYPE)

    def __str__(self):
        return "{} {}".format(self.name, self.description)


class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.name)
