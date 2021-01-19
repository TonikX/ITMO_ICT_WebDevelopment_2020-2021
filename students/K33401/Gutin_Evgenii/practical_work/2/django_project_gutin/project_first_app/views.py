from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Vehicle
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import VehicleForm, OwnerForm


def get_owner_by_id(request, owner_id):
    owners = [get_object_or_404(User, pk=owner_id)]
    return render(request, 'owner.html', {"owners": owners})


def get_owners(request):
    owners = User.objects.all()
    return render(request, 'owner.html', {"owners": owners})


def create_owner(request):
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/owners/all')
    return render(request, "owner_form.html", {"form": form})


class VehicleView(ListView):
    model = Vehicle
    template_name = 'vehicle.html'

    def get_queryset(self):
        param = self.request.GET.get('vehicle')
        if not param:
            return self.model.objects.all()
        else:
            try:
                vehicle_id = int(param)
                queryset = self.queryset.filter(pk=vehicle_id)
            except Exception:
                queryset = self.model.objects.none()
            return queryset


class VehicleDelete(DeleteView):
    model = Vehicle
    template_name = 'delete.html'
    success_url = '/vehicle/'


class VehicleUpdate(UpdateView):
    template_name = 'vehicle_form.html'
    model = Vehicle
    form_class = VehicleForm
    success_url = '/vehicle/'


class VehicleCreate(CreateView):
    template_name = 'vehicle_form.html'
    model = Vehicle
    form_class = VehicleForm
    success_url = '/vehicle/'
