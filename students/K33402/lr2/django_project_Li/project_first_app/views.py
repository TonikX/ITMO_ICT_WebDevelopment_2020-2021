from django.shortcuts import render, redirect
from .models import Driver
from .models import Car
from .models import Possession
from .models import DriverDocument
from .forms import DriverForm, CarForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
# Create your views here.

def driverF(requset):
    driver = Driver.objects.all()
    return render(requset, 'project_first_app/Driver.html', {'driver':driver})

def addDrivers(request):
    error = ''
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('Drivers')
        else:
            error = 'Форма не валидна'
    form = DriverForm()
    context={
        'form': form,
        'error': error
    }
    return render(request, 'project_first_app/addDrivers.html', context)


def CarF(requset):
    car = Car.objects.all()
    return render(requset, 'project_first_app/Car.html', {'car':car})


class CarCreate(CreateView):
    model = Car
    template_name = 'project_first_app/car_create_view.html'
    fields = ['id_number', 'model', 'label', 'color']


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'project_first_app/car_confirm_delete.html'

class CarUpdateView(UpdateView):
    model = Car
    fields = ['id_number', 'model', 'label', 'color']
    template_name = 'project_first_app/car_form.html'


def PossessionF(requset):
    possession = Possession.objects.all()
    return render(requset, 'project_first_app/Possession.html', {'possession':possession})


def DriverDocumentF(requset):
    driverDocument = DriverDocument.objects.all()
    return render(requset, 'project_first_app/DriverDocument.html', {'driverDocument':driverDocument})
