from django.shortcuts import render
from django.http import Http404
from .models import Driver, Car
from .forms import AddDriver
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


def driver(request, driver_id):
    try:
        p = Driver.objects.get(pk=driver_id)
    except Driver.DoesNotExist:
        raise Http404("Driver does not exist")
    return render(request, 'driver.html', {'driver': p})


def alldrivers(request):
    drivers = {"drivers": Driver.objects.all()}

    return render(request, 'alldrivers.html', drivers)

def add_driver(request):
    context = {}
    form = AddDriver(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_driver.html", context)


class Allcars(ListView):
    model = Car
    template_name = 'allcars.html'


class Car(DetailView):
    model = Car
    template_name = 'car.html'


class UpdateCar(UpdateView):
    model = Car
    template_name = 'update_car.html'
    fields = ['brand', 'model', 'color', 'number']
    success_url = '/allcars/'


class AddCar(CreateView):
    model = Car
    template_name = 'add_car.html'
    fields = ['brand', 'model', 'color', 'number']


class DeleteCar(DeleteView):
    model = Car
    success_url = '/allcars/'
    template_name = 'delete_car.html'







