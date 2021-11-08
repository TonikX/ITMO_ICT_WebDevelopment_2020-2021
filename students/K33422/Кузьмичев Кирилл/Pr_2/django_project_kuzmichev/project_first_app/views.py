from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CarOwnerForm


def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404('No such owner')
    return render(request, 'owner.html', {'owner': owner})


def get_carowners(request):
    carowners = CarOwner.objects.all()
    return render(request, 'carowners.html', {'carowners': carowners})


def create_carowner(request):
    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/carowners/')
    return render(request, 'create_carowner.html', {'form': form})


class CarList(ListView):
    model = Car
    template_name = 'car_list_view.html'


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['l_plate', 'brand', 'model', 'color']
    success_url = '/car/list/'
    template_name = 'car_form.html'


class CarCreateView(CreateView):
    model = Car
    fields = ['l_plate', 'brand', 'model', 'color']
    success_url = '/car/list/'
    template_name = 'car_form.html'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car/list/'
    template_name = 'car_confirm_delete.html'
