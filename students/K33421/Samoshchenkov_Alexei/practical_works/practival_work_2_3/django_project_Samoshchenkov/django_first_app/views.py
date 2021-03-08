from django.http import Http404
from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django_first_app.models import *
from django_first_app.forms import *


def detail(request, id):
    try:
        owner = Driver.objects.get(id=id)
    except Driver.DoesNotExist:
        raise Http404('Driver does not exist!')
    return render(request, 'django_first_app/owner.html', {'owner':owner, })

def show_drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'django_first_app/drivers.html', {'drivers':drivers, })

def create_driver(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/drivers')
    return render(request, 'django_first_app/driver_c_form.html', {'form':form, })

class CarCreate(CreateView):
    model = Car
    fields = ['brand', 'model', 'colour', 'id_number']
    template_name_suffix = '_create'
    success_url = '/cars/'

class CarUpdate(UpdateView):
    model = Car
    fields = ['brand', 'model', 'colour', 'id_number']
    template_name_suffix = '_update'
    success_url = '/cars/'

class CarDelete(DeleteView):
    model = Car
    template_name_suffix = '_delete'
    success_url = '/cars/'

class CarList(ListView):
    model = Car
    context_object_name = 'car_list'

class CarDetail(DetailView):
    model = Car
    context_object_name = 'car'
