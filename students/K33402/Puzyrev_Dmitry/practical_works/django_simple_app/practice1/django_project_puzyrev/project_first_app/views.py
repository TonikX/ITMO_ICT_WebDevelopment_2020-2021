from django.shortcuts import render
from django.http import Http404
from project_first_app.models import *

def detail(request, id):

  try:
    owner = Driver.objects.get(id=id)
  except Driver.DoesNotExist:
    raise Http404('Driver does not exist')

  return render(request, 'project_first_app/owner.html', {
    'owner': owner,
  })