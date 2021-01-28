from django.shortcuts import render
from .models import Owner
from .models import Car
from .forms import addOwner
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

def owner(request):
    return render(request, 'owners.html', {'owners': Owner.objects.all()})

class owner_id(DetailView):
    model = Owner
    template_name = 'owner.html'

class car_id(DetailView):
    model = Car
    template_name = 'car.html'

class car(ListView):
    model = Car
    template_name = 'cars.html'

class car_Update(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color', 'car_number']
    success_url = '/cars/'
    template_name = 'car_update.html'

def owner_create(request):
    context = {}
    form = addOwner(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'owners.html', {'owners': Owner.objects.all()})
    context['form'] = form
    return render(request, "owner_create.html", context)

class car_delete(DeleteView):
    model = Car
    template_name = 'car_delete_confirm.html'
    success_url = '/cars/'

class car_add(CreateView):
  model = Car
  template_name = 'car_add.html'
  fields = ['brand', 'model', 'color', 'car_number']
  success_url = '/cars/'
