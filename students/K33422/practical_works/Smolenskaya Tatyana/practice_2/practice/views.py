from django.shortcuts import render
from django.http import Http404
from .models import *
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import DriverForm


def get_driver(request, driver_id):
    try:
        driver = Driver.objects.get(pk=driver_id)
    except Driver.DoesNotExist:
        raise Http404('Driver doesn\'t exist')
    return render(request, 'driver.html', {'driver': driver})


def get_drivers(request):
    context = {"dataset": Driver.objects.all()}

    return render(request, "drivers.html", context)


class CarsListView(ListView):
    model = Car
    queryset = model.objects.all()
    template_name = "car_list.html"

    def get_queryset(self):
        driver = self.request.GET.get('driver')

        if driver:

            try:
                driver = int(driver)
                queryset = self.queryset.filter(ownership__driver=driver)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


class CarDetailView(DetailView):
    model = Car
    template_name = 'car.html'


def create_view(request):
    context = {}

    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_driver.html", context)


class CarUpdateView(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color', 'number']
    success_url = '/cars/'
    template_name = "car_update.html"


class CarCreate(CreateView):
    model = Car
    template_name = 'car_create_view.html'
    success_url = '/cars/'

    fields = ['brand', 'model', 'color', 'number']


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = '/cars/'
