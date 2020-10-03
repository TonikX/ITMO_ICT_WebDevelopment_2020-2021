from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Driver
from django.views.generic.list import ListView
from .models import Car
from .forms import DriverForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


def detail(request):
    context = {"drivers": Driver.objects.all()}
    return render(request, 'drivers.html', context)


class CarsList(ListView):
    model = Car
    template_name = 'car_list_view.html'


def create_driver_view(request):
    context = {}
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_driver_view.html", context)


class CarUpdateView(UpdateView):
    model = Car
    fields = ['id_number', 'session', 'model', 'label', 'color']
    success_url = '/cars/'
    template_name = 'car_form.html'


class CarCreate(CreateView):
    model = Car
    template_name = 'car_create_view.html'
    fields = ['id_number', 'session', 'model', 'label', 'color']
    success_url = '/cars/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = '/cars/'
