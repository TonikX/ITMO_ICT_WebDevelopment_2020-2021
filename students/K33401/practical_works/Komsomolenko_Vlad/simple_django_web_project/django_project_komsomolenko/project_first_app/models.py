from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    car_number = models.IntegerField()

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()

class Possession(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class License(models.Model):
    typeLicense = [
        ('M', 'M'),
        ('A1', 'A1'),
        ('A', 'A'),
        ('B1', 'B1'),
        ('B', 'B'),
        ('BE', 'BE'),
        ('C', 'C'),
        ('C1', 'C1'),
        ('CE', 'CE'),
        ('CE1', 'CE1'),
        ('D', 'D'),
        ('D1', 'D1'),
        ('DE', 'DE'),
        ('DE1', 'DE1'),
        ('TM', 'TM'),
        ('TB', 'TB'),
    ]
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    license_number = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=5, choices=typeLicense, default='M')