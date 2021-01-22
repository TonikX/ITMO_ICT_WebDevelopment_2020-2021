from django.db import models

class Driver(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)

class DriverLicense(models.Model):
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
    license_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()

class Car(models.Model):
    plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    owner = models.ManyToManyField(Driver, through='Hold', through_fields=('car', 'owner'))

class Hold(models.Model):
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    expiration_date = models.DateField()