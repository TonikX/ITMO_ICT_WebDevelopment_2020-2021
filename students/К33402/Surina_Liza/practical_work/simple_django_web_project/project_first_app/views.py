from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView

from .models import CarOwner, ExampleModel, Publisher, Car
from django.views.generic.detail import DetailView
from .forms import ExampleForm


class PublisherRetrieveView(DetailView):
  model = CarOwner


def detail(request, id):
    try:
        info = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'project_first_app/detail.html', {'info': info})


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь
    context["dataset"] = ExampleModel.objects.all()

    return render(request, "project_first_app/list_view.html", context)


class ExampleList(ListView):
    # specify the model for list view
    model = ExampleModel
    template_name = 'project_first_app/cvb_list_view.html'


def create_view(request):

    context = {}
    form = ExampleForm(request.POST or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarOwnerUpdateView(UpdateView):
    model = CarOwner
    fields = ["first_name", "last_name", "birthday"]
    success_url = '/car_owner/'


class CarCreate(CreateView):
    model = Car
    template_name = 'cvb_create_view.html'

    fields = ['G_num', 'mark', 'model_car', 'color']