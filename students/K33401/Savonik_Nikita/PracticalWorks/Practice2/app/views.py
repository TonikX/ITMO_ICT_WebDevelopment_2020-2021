from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import CarOwnerForm

class IndexView(TemplateView):
  template_name = "index.html"


def car_owner_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Car_owner.objects.all()
    context["info"] = Owner_info.objects.all()

    return render(request, "car_owner_list.html", context)

def car_owner_create_view(request):
    context = {}
    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'car_owner_form.html', context)



class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color', 'number']
    template_name = 'car_form.html'
    success_url = '/cars'

class CarCreateView(CreateView):
    model = Car
    fields = ['brand', 'model', 'color', 'number']
    template_name = 'car_form.html'
    success_url = '/cars'

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars'
