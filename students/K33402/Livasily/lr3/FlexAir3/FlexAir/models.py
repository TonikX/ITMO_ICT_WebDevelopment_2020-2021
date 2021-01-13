from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.



class Airline(models.Model):  # Авиакомпания
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="airlines", null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Airport(models.Model):  # Аэропорт
    class Meta:
        unique_together = (('company', 'city', 'airaport'),)

    company = models.ForeignKey(Airline, on_delete=models.CASCADE, verbose_name="Компания")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    airaport = models.CharField(max_length=30, verbose_name="Аэропорт")

    def __str__(self):
        return "Компания: {}, Город: {}, Аэропорт: {}".format(self.company, self.city, self.airaport)


# class Arrival(models.Model): # прилет
#     id = models.AutoField(primary_key=True)
#     arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, verbose_name="Прилет")  # куда летим
#
#     def __str__(self):
#         return "{}".format(self.arrival)

#
# class Departure(models.Model):  # отлет
#     id = models.AutoField(primary_key=True)
#     departure = models.ForeignKey(Airport, on_delete=models.CASCADE, verbose_name="отлет")  # откуда летим
#
#     def __str__(self):
#         return "{}".format(self.departure)
#
#
# class Route(models.Model):  # Путь
#     id = models.AutoField(primary_key=True)
#     departure = models.ForeignKey(Departure, on_delete=models.CASCADE, related_name="отлет")  # откуда летим
#     arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE, related_name="Прилет")  # куда летим
#     dateDeparture = models.DateTimeField()
#     dateArrival = models.DateTimeField()
#     distance = models.PositiveIntegerField()  # Расстояние в метрах
#
#     # def has_add_permission(self, request):
#     #     num_objects = self.model.objects.count()
#     #     if num_objects >= 1:
#     #         return False
#     #     else:
#     #         return True
#
#
# class Flight(models.Model):  # Рейс
#     id = models.CharField(primary_key=True, max_length=50)
#     airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
#     Transit = models.BooleanField()
#     courses = models.ManyToManyField(Route)
#     def __str__(self):
#         return "{} {}".format(self.airline, self.id)
#
#
# class Plane(models.Model):  # Самолет
#     id = models.AutoField(primary_key=True)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     countPlace = models.PositiveSmallIntegerField()
#     def __str__(self):
#         return "id: {}; Компания: {}; Мест: {}".format(self.id, self.flight, self.countPlace)
#
#
# class Board(models.Model):  # Борт
#     id = models.AutoField(primary_key=True)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#
#
# class FlightAttendant(models.Model):  # Борт проводник
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendant")
#     education = (
#         ('I', 'ITMO'),
#         ('S', 'SPBGU'),
#         ('D', 'DVFU'),
#     )
#     Education = models.CharField(max_length=1, choices=education, verbose_name='Об')
#     Experience = models.PositiveSmallIntegerField()
#     board = models.ManyToManyField(Board)
#
#     def __str__(self):
#         return "{} {}".format(self.user, self.Education)
#
#
# class Pilot(models.Model):  # Пилот
#     education_type = [
#         ('1', 'Pilot'),
#         ('2', 'SecondPilot'),
#         ('3', 'Navigator'),
#     ]
#     education = models.CharField(
#         max_length=1,
#         choices=education_type,
#         verbose_name="должность"
#     )
#     # passport = models.CharField(max_length=10, primary_key=True)
#     # FIO = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pilot")
#     Experience = models.PositiveSmallIntegerField()
#     board = models.ManyToManyField(Board)
#
#     def __str__(self):
#         return "{} {}".format(self.user, self.education)
