from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from project_first_app.models import *
from project_first_app.form import DriverForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView


def all_drivers(request):
	drivers = Driver.objects.all()

	return render(request, 'project_first_app/drivers.html', {
		'drivers': drivers
	})

def create_driver(request):
	form = DriverForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/drivers')
	return render(request, "project_first_app/driver_create_form.html", {"form": form})

class CarList(ListView):
	model = Car
	context_object_name = 'all_cars'


class CarDetail(DetailView):
	model = Car
	context_object_name = 'car'


class CarCreate(CreateView):
	model = Car
	fields = ['brand', 'model', 'color', 'official_number']
	template_name_suffix = '_create_form'
	success_url = '/cars/'


class CarUpdate(UpdateView):
	model = Car
	fields = ['brand', 'model', 'color', 'official_number']
	template_name_suffix = '_update_form'
	success_url = '/cars/'


class CarDelete(DeleteView):
	model = Car
	success_url = '/cars/'