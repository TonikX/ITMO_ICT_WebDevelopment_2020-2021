from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from project_first_app.forms import AddOwnerForm
from project_first_app.models import Car
from project_first_app.models import Owner


def owner(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)

    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})


def owners(request):
    context = {}
    context["dataset"] = Owner.objects.all()
    return render(request, "all_owners.html", context)


def car(request, car_id):
    try:
        p = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, 'car.html', {'Car': p})


class Cars(ListView):
    model = Car
    template_name = 'cars.html'


class CarsUpdate(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = ['brand', 'model', 'color', 'gov_number', 'owner']
    success_url = '/owners/'


class CarsCreate(CreateView):
    model = Car
    template_name = 'cars_add.html'
    fields = ['brand', 'model', 'color', 'gov_number', 'owner']


class CarsDelete(DeleteView):
    model = Car
    template_name = 'cars_delete.html'
    success_url = '/owners/'


def add_owners(request):
    context = {}
    form = AddOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_add.html", context)
