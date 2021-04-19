from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import *
from .forms import CarOwnerForm


def get_owner(request, owner_id):
    try:
        car_owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404('Owner doesn\'t exist')
    return render(request, 'owner.html', {'owner': car_owner})


def get_owners(request):
    context = {'dataset': CarOwner.objects.all()}

    return render(request, 'owners_list.html', context)


class CarsList(ListView):
    model = Car
    template_name = 'cars_list.html'


class CarDetails(DetailView):
    model = Car
    template_name = 'car.html'


def create_view(request):
    form = CarOwnerForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'owner_creating.html', context)


class CarCreate(CreateView):
    model = Car
    fields = ['state_number', 'brand', 'model', 'color']
    success_url = '/cars_list/'
    template_name = 'car_creating.html'


class CarUpdate(UpdateView):
    model = Car
    fields = ['state_number', 'brand', 'model', 'color']
    success_url = '/cars_list/'
    template_name = 'car_updating.html'


class CarDelete(DeleteView):
    model = Car
    success_url = '/cars_list/'
    template_name = 'car_deleting.html'
