from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import render
from .models import Car, Driver


def get_owner_by_id(request, owner_id):
    try:
        owner = Driver.objects.get(pk=owner_id)
    except Driver.DoesNotExist:
        raise Http404("such owner doesn't exist")
    return render(request, 'owner_id.html', {"owner": owner})