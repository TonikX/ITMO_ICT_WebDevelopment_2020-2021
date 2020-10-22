from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import CarOwnerForm
from .models import *

# Create your views here.

def owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404('Owner does not exist')
    return render(request, 'owner.html', {'owner': owner})

def owners(request):
    context = {"dataset": Owner.objects.all()}
    return render(request, "owners.html", context)

class CarsListView(ListView):
    model = Car
    queryset = model.objects.all()
    template_name = "car_list.html"

    def queryset(self):
        owner = self.request.GET.get('owner')

        if owner:

            try:
                owner = int(owner)
                queryset = self.queryset.filter(ownership__owner=owner)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset

class CarDetailView(DetailView):
    model = Car
    template_name = 'car.html'

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)

class CarUpdateView(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color', 'license_plate']
    success_url = '/cars/'
    template_name = "car_update.html"

class CarCreate(CreateView):
    model = Car
    template_name = 'car_create_view.html'
    success_url = '/cars/'

    fields = ['brand', 'model', 'color', 'license_plate']

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = '/cars/'