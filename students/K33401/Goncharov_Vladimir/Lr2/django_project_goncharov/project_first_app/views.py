from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from project_first_app.models import Driver


class DriverDetailView(DetailView):
    model = Driver
    template_name = 'driver_detail.html'
