from django.shortcuts import render
from django.http import Http404
from project_first_app.models import *
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import CarownerAddForm
# Create your views here.


def CarownerView(request, carowner_id):
    try:
        p = Carowner.objects.get(pk=carowner_id)
    except Carowner.DoesNotExist:
        raise Http404("Carowner does not exist")
    return render(request, 'carowner_id.html', {'carowner': p})


def CarView(request, car_id):
    try:
        p = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, 'car_id.html', {'car': p})


def CarownerListView(request):
    context = {}
    context["dataset"] = Carowner.objects.all()[1:]
    return render(request, "carowner_list.html", context)


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarAddView(CreateView):
    model = Car
    fields = ['mark', 'carmodel', 'color', 'number']
    template_name = 'car_add.html'


class CarEditView(UpdateView):
    model = Car
    fields = ['mark', 'carmodel', 'color', 'number']
    template_name = 'car_edit.html'
    success_url = '/car_list/'


class CarDelView(DeleteView):
    model = Car
    fields = ['mark', 'carmodel', 'color', 'number']
    template_name = 'car_del.html'
    success_url = '/car_list/'


def CarownerAdd(request):
    context = {}
    form = CarownerAddForm(request.POST or None)
    if form.is_valid():
        form.save
    context['form'] = form
    return render(request, "carowner_add.html", context)
