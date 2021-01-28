from django.http import Http404
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import User, Car, Possession
from .forms import CarCreationForm, UserCreationForm

# Create your views here.
def get_car_owner(request, car_id):
    try:
        possession = Possession.objects.get(car=car_id)
        print(possession.car_owner)
    
    except Possession.DoesNotExist:
        raise Http404("Car doesn't exist")

    return render(request, 'project_first_app/owner_detail.html', {'owner': possession.car_owner})

def get_owners(request):
    try:
        owners = User.objects.all()
    except User.DoesNotExist:
        raise Http404("Owners doesn't exists")

    return render(request, 'project_first_app/owner_list.html', {'owners': owners})

def get_owner(request, id):
    try:
        owner = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404("Car owner doesn't exist")

    return render(request, 'project_first_app/owner_detail.html', {'owner': owner})

class CarList(ListView):

    model=Car

class CarDetailView(DetailView):

    model=Car

def owner_create_view(request):
    
    context= {}
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "project_first_app/owner_create_view.html", context)

class CarCreateView(CreateView):
    model=Car
    template_name='project_first_app/car_create_view.html'
    fields=[
            "brand",
            "car_model",
            "color",
            "number"
    ]
    success_url='/cars/'

class CarUpdateView(UpdateView):
    model=Car
    fields=[
            "brand",
            "car_model",
            "color",
            "number"
    ]
    success_url='/cars/'

class CarRemoveView(DeleteView):
    model=Car
    success_url='/cars/'

