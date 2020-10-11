from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from project_first_app.form import DriverForm
from .models import Driver, Car


# Create your views here.

def all_drivers_detail(request):
    context = {"drivers": Driver.objects.all(), "all": True}

    return render(request, 'drivers.html', context)


def driver_detail(request, driver_id):
    context = get_object_or_404(Driver, pk=driver_id)

    return render(request, 'drivers.html', {"driver": context, "one": True})


def create_driver(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/drivers')
    return render(request, "drivers.html", {"form": form, "new": True})


class AllCars(ListView):
    model = Car
    template_name = "cars.html"


class OneCar(DetailView):
    model = Car
    template_name = "cars.html"


class CarDelete(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = '/cars/'


class CarCreate(CreateView):
    model = Car
    template_name = 'car_create_update.html'
    fields = ['id_number', 'brand', 'car_model', 'color', 'official_number']
    success_url = '/cars/'


class CarUpdate(UpdateView):
    model = Car
    fields = ['id_number','brand', 'car_model', 'color', 'official_number']
    success_url = '/cars/'
    template_name = 'car_create_update.html'

