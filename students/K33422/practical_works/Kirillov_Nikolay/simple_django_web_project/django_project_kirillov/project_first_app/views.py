from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import *
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import AddDriverForm


class CarCreate(CreateView):
    model = Car
    template_name = 'car_add.html'
    fields = ['brand', 'model', 'color', 'number', 'owner']


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = ['brand', 'model', 'color', 'number', 'owner']
    success_url = '/driver/list/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/driver/list/'


class CarListView(ListView):
    model = Car
    template_name = 'car_list_view.html'


def CarDetail(request, car_id):
    try:
        p = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, 'car.html', {'Car': p})


def DriverCreate(request):
    context = {}
    form = AddDriverForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "driver_add.html", context)


def DriverListView(request):
    context = {}
    context["dataset"] = Driver.objects.all()[1:]
    return render(request, "driver_list_view.html", context)


def DriverDetail(request, driver_id):
    try:
        p = Driver.objects.get(pk=driver_id+2)
    except Driver.DoesNotExist:
        raise Http404("Driver does not exist")
    return render(request, 'driver.html', {'driver': p})
