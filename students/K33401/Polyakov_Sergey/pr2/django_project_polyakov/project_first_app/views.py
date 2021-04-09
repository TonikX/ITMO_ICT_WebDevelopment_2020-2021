from django.shortcuts import render
from django.http import Http404
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from .models import Owner, Car
from .forms import OwnerForm


class IndexPage(View):
    template_name = 'project_first_app/index.html'

    def get(self, request):
        return render(request, self.template_name)


def owner_detail_view(request, id):
    template_name = 'project_first_app/owner_detail.html'

    try:
        owner = Owner.objects.get(id=id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, template_name, {'owner': owner})


def owners_list_view(request):
    template_name = 'project_first_app/owners_list.html'

    context = {'owners_list': Owner.objects.all()}

    return render(request, template_name, context)


def owner_create_view(request):
    template_name = 'project_first_app/owner_create.html'

    context = {}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, template_name, context)


class CarDetailView(DetailView):
    model = Car
    template_name = 'project_first_app/car_detail.html'


class CarsListView(ListView):
    model = Car
    template_name = 'project_first_app/cars_list.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['licence_number', 'make', 'model', 'color']
    success_url = '/cars/'
    template_name = 'project_first_app/car_update.html'


class CarCreateView(CreateView):
    model = Car
    fields = [ 'licence_number', 'make', 'model', 'color']
    success_url = '/cars/'
    template_name = 'project_first_app/car_create.html'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'project_first_app/car_delete.html'
