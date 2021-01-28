from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Resident(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    passport = models.CharField(max_length=10, unique=True)
    arrival_city = models.CharField(max_length=100)
    check_in = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} | {self.arrival_city} | {self.check_in}'


class Room(models.Model):
    ROOM_TYPE = (
        ('3', 'Triple'),
        ('2', 'Double'),
        ('1', 'Single')
    )
    type = models.CharField(max_length=1, choices=ROOM_TYPE)
    price = models.IntegerField(default=1000)
    floor = models.IntegerField(default=1)
    number = models.IntegerField(default=100)
    telephone = models.CharField(max_length=10, unique=True)
    cleaners = models.ManyToManyField('Employee', through='CleaningSchedule')
    is_vacant = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.number} | {self.type}'


class BookingRecord(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.PROTECT, related_name='booking_details')
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField(null=True, blank=True)
    total_bill = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.resident.last_name}'


class CleaningSchedule(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cleaner')
    staff = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='staff')
    date_time = models.DateTimeField()

    def __str__(self):
        return f'{self.staff.last_name} - {self.date_time}'
