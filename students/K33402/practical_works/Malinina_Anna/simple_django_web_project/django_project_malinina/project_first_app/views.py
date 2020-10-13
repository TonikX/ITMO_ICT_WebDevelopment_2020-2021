from django.shortcuts import render
from django.http import Http404
from .models import *


def get_owner(request, owner_id):
    try:
        car_owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404('Owner doesn\'t exist')
    return render(request, 'owner.html', {'owner': car_owner})
