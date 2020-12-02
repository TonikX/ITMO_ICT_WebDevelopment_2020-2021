from django.shortcuts import render
from .models import CarOwner
from .models import Car
from .forms import OwnerForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

# Представление на основе функций

def owners_list(request):

    context ={}

    context["dataset"] = CarOwner.objects.all()

    return render(request, 'owners_list.html', context)


# Представление на основе классов(все объекты)

class cars_list(ListView):
    model = Car
    template_name = 'cars_list.html'


# Представление на основе классов(один объект)

class car_detail(DetailView):
    model = Car
    template_name = 'car_detail.html'

# Переопределение стандартных методов в generic view

class CarListView(ListView):
    model = Car
    template_name = 'car_list_view.html'
    queryset = model.objects.all()

    def get_queryset(self):

        car = self.request.GET.get('car')

        if car:
            try:
                car = int(car)
                queryset = self.queryset.filter(car=car)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset




# формы
def add_car_owner(request):
    context ={}

    form = OwnerForm(request.POST or None)

    if form.is_valid():

        form.save()

    context['form'] = form

    return render(request, "add_car_owner.html", context)


# Обновление объекта по первичному ключу

from django.views.generic.edit import UpdateView

class CarUpdate(UpdateView):
  model = Car
  fields = ['reg_num','color', 'brand', 'model']
  success_url = '/cars_list/'
  template_name = 'car_update.html'

# Создание объекта

class CarCreate(CreateView):

   # specify the model for create view
   model = Car
   template_name = 'car_create.html'
   # specify the fields to be displayed

   fields = ['reg_num','color', 'brand', 'model']

# Удаление объекта

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars_list/'
  template_name = 'car_delete.html'