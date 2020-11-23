from django.shortcuts import render
from django.http import Http404
from cars.models import Owner, Car, Ownership, DrivingLicense
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import OwnerForm


def owner(request, owner_id):
    context = {'owner': Owner.objects.get(pk=owner_id)}
    return render(request, 'cars/owner.html', context)


def owners_list(request):
    context = {'owners': Owner.objects.all()}
    return render(request, 'cars/owners_list.html', context)


def create_owner(request):
    context = dict()
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "cars/create_owner.html", context)


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'


class CarListView(ListView):
    model = Car
    queryset = Car.objects.all()
    template_name = 'cars/cars_list.html'

    def get_queryset(self):
        license_plate = self.request.GET.get('license_plate')
        if license_plate:
            try:
                queryset = self.queryset.filter(license_plate=license_plate)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset

        return self.queryset


class CarCreateView(CreateView):
    model = Car
    fields = ['brand', 'model', 'color', 'license_plate']
    template_name = 'cars/create_car.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color']
    success_url = '/cars/'
    template_name = 'cars/car_form.html'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_delete.html'
    success_url = '/cars/'
