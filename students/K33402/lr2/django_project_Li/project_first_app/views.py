from django.shortcuts import render
from .models import Driver
from .models import Car
from .models import Possession
from .models import DriverDocument
# Create your views here.

def driverF(requset):
    driver = Driver.objects.all()
    return render(requset, 'project_first_app/Driver.html', {'driver':driver})
