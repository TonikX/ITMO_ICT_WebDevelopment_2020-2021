from django.shortcuts import render
from .models import Person, Car, DriverLicence, Ownership
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import AddPerson

def owner(request, number):
    owner = Person.objects.all()[number - 1]
    return render(request, 'owner.html', { 'name': owner.name, 'surname': owner.surname, 'birthday': owner.birthday })
    
def owners(request):
    context = {}
    context["dataset"] = Person.objects.all()
    return render(request, 'owners.html', context)
        
def add_person(request):
    context = {}
    form = AddPerson(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'add_person.html', context)
    
class CarsList(ListView):
    model = Car
    template_name = 'cars.html'
    
class CarDetail(DetailView):
    model = Car
    template_name = 'car.html'
    
class UpdateCar(UpdateView):
    model = Car
    fields = ['color', 'number', 'owner']
    success_url = '/cars/'
    template_name = 'update_car.html'
    
class DeleteCar(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'delete_car.html'
    
class AddCar(CreateView):
    model = Car
    fields = ['brand', 'model', 'color', 'number', 'owner']
    success_url = '/cars/'
    
    template_name = 'add_car.html'