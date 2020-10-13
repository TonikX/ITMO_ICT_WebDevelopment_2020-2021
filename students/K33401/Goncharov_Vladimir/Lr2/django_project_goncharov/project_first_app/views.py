from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from project_first_app.forms import DriverForm
from project_first_app.models import Driver, Car


class DriverDetailView(DetailView):
    model = Driver
    template_name = 'driver_detail.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarsList(ListView):
    model = Car
    template_name = 'car_list_view.html'


def create_driver_view(request):
    context = {}
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "driver_create.html", context)


class CarUpdateView(UpdateView):
    model = Car
    fields = ['id_number', 'model', 'label', 'color']
    success_url = '/car/'
    template_name = 'car_update.html'


class CarCreate(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['id_number', 'model', 'label', 'color']
    success_url = '/car/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/car/'
