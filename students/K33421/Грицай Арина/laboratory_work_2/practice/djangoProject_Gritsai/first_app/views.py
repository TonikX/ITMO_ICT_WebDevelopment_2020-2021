from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from first_app.models import Owner, Vehicle
from first_app.form import OwnerForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


# Create your views here.
def owner(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})


def all_owners(request):
    visual = {"owners": Owner.objects.all()}
    return render(request, 'all_owners.html', visual)


class vehicleView(DetailView):
    model = Vehicle
    template_name = 'vehicle.html'


def all_vehicles(request):
    visual = {"vehicles": Vehicle.objects.all()}
    return render(request, 'all_vehicles.html', visual)


class upd_vehicleView(UpdateView):
    model = Vehicle
    fields = ['id', 'brand', 'model', 'color', 'reg_number', 'owning']
    success_url = '/all_vehicles/'
    template_name = 'upd_vehicle.html'


def add_ownerView(request):
    visual = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    visual['form'] = form
    return render(request, 'add_owner.html', visual)


class add_vehicle(CreateView):
    model = Vehicle
    template_name = 'add_vehicle.html'
    fields = ['id', 'brand', 'model', 'color', 'reg_number', 'owning']
    success_url = '/all_vehicles/'


class del_vehicleView(DeleteView):
    model = Vehicle
    success_url = '/all_vehicles/'
    template_name = 'del_vehicle.html'
