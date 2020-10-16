from django.shortcuts import render
from .models import Person, Car, DriverLicence, Ownership
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import AddPerson

def homeworks(request):
    context = {}
    context["dataset"] = Homework.objects.all()
    return render(request, 'homeworks.html', context)