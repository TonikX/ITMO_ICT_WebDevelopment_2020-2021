from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    b_date = models.DateField()


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.IntegerField()
    session = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return "{} {}".format(self.brand, self.model)


class Ownership(models.Model):
    car_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self):
        return "{} {} {}".format(self.car_owner, self.car, self.start_date)


class Licence(models.Model):
    l_number = models.IntegerField()
    date = models.DateField()
    owner_car = models.ForeignKey(Owner, on_delete=models.CASCADE)
    TYPE = (
        ('a1', 'first'),
        ('b2', 'sec'),
    )
