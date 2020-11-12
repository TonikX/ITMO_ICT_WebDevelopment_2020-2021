from django.http import Http404
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Owner, Car
from .forms import AddOwner


def index(request):
    return render(request, 'index.html')


def get_owner_data(request, id):  # отдельная страничка владельца функционально
    try:
        o = Owner.objects.get(id=id)
    except Owner.DoesNotExist:
        raise Http404("owner does not exist")
    return render(request, 'owner.html', {'owner': o})


def get_all_owners(request):  # вывод всех владельцев функционально
    context = {}
    context['owners'] = Owner.objects.all()
    return render(request, 'fun_owners_list.html', context)


def add_owner(request):  # ввод владельца функционально
    context = {}

    form = AddOwner(request.POST or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'add_owner.html', context)


class GetCarData(DetailView):  # отдельная страница авто классом

    model = Car
    template_name = 'car.html'
    context_object_name = 'car'


class GetAllCars(ListView):  # вывод всех авто классом

    model = Car
    template_name = 'cars_list.html'
    context_object_name = 'cars'


class AddCar(CreateView):  # добавить авто классом

    model = Car
    template_name = 'add_car.html'
    fields = [
        'brand',
        'model',
        'color',
        'plate_number'
    ]
    success_url = reverse_lazy('cars_list')


class UpdateCar(UpdateView):  # обновить авто классом

    model = Car
    template_name = 'update_car.html'
    fields = [
        'brand',
        'model',
        'color',
        'plate_number'
    ]
    success_url = reverse_lazy('cars_list')


class DeleteCar(DeleteView):  # удалить авто классом

    model = Car
    template_name = 'delete_car.html'

    success_url = reverse_lazy('cars_list')
