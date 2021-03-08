from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    passport = models.CharField(max_length=10)
    driving_class = models.IntegerField()
    experience = models.IntegerField()
    salary = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        if not self.salary:
            self.salary = 45000 + self.experience * 1000 + self.driving_class * 500
        super(Driver, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'


class Route(models.Model):
    number = models.IntegerField(primary_key=True)
    departure_name = models.CharField(max_length=50)
    destination_name = models.CharField(max_length=50)
    departure_time = models.TimeField()
    destination_time = models.TimeField()
    interval_min = models.IntegerField()
    duration_min = models.IntegerField()


class Bus(models.Model):
    number = models.CharField(max_length=6, primary_key=True)
    bus_type = models.IntegerField(
        choices=(
            (1000, 'Автозак'),
            (20, 'Газель')
        )
    )
    capacity = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        if self.capacity is None:
            self.capacity = self.bus_type
        self.number = self.number.upper()
        super(Bus, self).save(*args, **kwargs)


class Shift(models.Model):
    date = models.DateField()
    driver = models.ForeignKey(to=Driver, on_delete=models.SET_NULL, null=True)
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)
