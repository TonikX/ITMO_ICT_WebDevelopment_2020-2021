from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()


class Driver_licence(models.Model):
    LICENCE_TYPE = (('A', 'Мотоцикл'), ('B', 'Автомобиль'), ('C', 'Грузовики'), ('D', 'Автобус'))
    driver = models.ForeignKey("Owner", on_delete=models.CASCADE)
    given_date = models.DateField()
    type = models.CharField(max_length=1, choices=LICENCE_TYPE)


# ok
class Auto(models.Model):
    having = models.ManyToManyField(Owner, through='Ownership')
    brend = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.model, self.brend)


# ok
class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
