from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
import datetime

from django.shortcuts import render

from project_first_app.forms import OwnerForm
from project_first_app.models import Owner
from project_first_app.models import Car

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


# from .forms import OwnerForm


def owners(request):
    info = {"owners": Owner.objects.all()}
    return render(request, 'owner.html', info)


class OwnerDetails(DetailView):
    model = Owner
    template_name = 'owner_details.html'


class Cars(ListView):
    model = Car
    template_name = 'cars.html'


class CarDetails(DetailView):
    model = Car
    template_name = 'car_details.html'


def create_owner(request):
    context = {}

    form = OwnerForm(request.POST or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_owner.html", context)


class create_car(CreateView):
    model = Car
    template_name = 'create_car.html'
    fields = ['brand', 'model', 'color', 'num']


class update_car(UpdateView):
    model = Car
    template_name = 'update_car.html'
    fields = ['brand', 'model', 'color', 'num']


class delete_car(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/cars/'

