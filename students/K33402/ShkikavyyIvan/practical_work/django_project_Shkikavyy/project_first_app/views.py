from django.shortcuts import render
from django.http import Http404
from project_first_app.models import Owner
from django.views.generic.list import ListView
from .models import Auto
from .forms import OwnerForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


# Create your views here.

def name(request, owner_id):
    try:
        driver = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': driver})


class AutoDetailView(DetailView):
    model = Auto
    template_name = 'auto_detail.html'


def detail(request):
    context = {"owners": Owner.objects.all}
    return render(request, 'owner.html', context)


class AutoList(ListView):
    model = Auto
    template_name = 'auto_list_view.html'


def create_owner_view(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owner_view.html", context)


class AutoUpdateView(UpdateView):
    model = Auto
    fields = ['having', 'brend', 'model', 'color']
    success_url = '/autos/'
    template_name = 'auto_form.html'


class AutoCreate(CreateView):
    model = Auto
    fields = [ 'having', 'brend', 'model', 'color']
    success_url = '/autos/'
    template_name = 'auto_create_view.html'


class AutoDeleteView(DeleteView):
    model = Auto
    success_url = '/autos/'
    template_name = 'auto_confirm_delete.html'
