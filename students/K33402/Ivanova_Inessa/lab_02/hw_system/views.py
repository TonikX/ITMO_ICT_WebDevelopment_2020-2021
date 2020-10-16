from django.shortcuts import render
from .models import User, Homework, Assignment
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

def homeworks(request):
    context = {}
    context["dataset"] = Homework.objects.all()
    return render(request, 'homeworks.html', context)