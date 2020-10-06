from django.shortcuts import render
from .models import Owner
from django.views.generic.detail import DetailView

def owner(request):
    return render(request, 'owners.html', {'owners': Owner.objects.all()})

class owner_id(DetailView):
    model = Owner
    template_name = 'owner.html'