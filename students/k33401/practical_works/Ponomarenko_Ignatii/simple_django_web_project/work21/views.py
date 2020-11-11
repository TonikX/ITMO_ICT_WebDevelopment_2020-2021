from django.http import Http404

from django.shortcuts import render

from work21.models import CarOwner, Car

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import CarOwnerForm


def detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'work21/owner.html', {'owner': p})

class CarDetail(DetailView):
	model = Car

def owner_list(request):
	owners = CarOwner.objects.all()
	return render(request, 'work21/owners_list.html', {'owners': owners})

class CarListView(ListView):
	model = Car
    
def car_owner_create(request):
    context ={}

    form = CarOwnerForm(request.POST or None) # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid(): # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "work21/car_owner_create.html", context)

class CarCreate(CreateView):
    model = Car
    template_name = 'work21/car_create.html'
    fields = [
        'brand',
        'model',
        'color',
        'number',
    ]
    success_url = '/car/list'

class CarUpdate(UpdateView):
    model = Car
    template_name = 'work21/car_create.html'
    fields = [
        'brand',
        'model',
        'color',
        'number',
    ]
    success_url = '/car/list'

class CarDelete(DeleteView):
  model = Car
  success_url = '/car/list'