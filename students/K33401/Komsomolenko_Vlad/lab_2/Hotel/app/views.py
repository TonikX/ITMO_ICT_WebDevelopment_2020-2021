import kwargs as kwargs
import now as now
from django.http import HttpResponseRedirect
from django.shortcuts import render
from accounts.models import Hotel, Room, Feedback, Reserve
from .forms import addFeedback, addReserve
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django import forms


def loginPass(request):
    if request.user.type == 'user':
        return render(request, 'user.html')
    else:
        return render(request, 'admin.html')


class Hotels(ListView):
    model = Hotel
    template_name = 'user_hotels.html'


def rooms(request, hotel):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    context["hotel"] = hotel
    context["rooms"] = Room.objects.all()

    return render(request, "rooms.html", context)


class RoomDetail(DetailView):
    model = Room
    template_name = 'room.html'


class RepertoireModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.id)


def feedback(request, hotel):
    context = {}
    context["hotel"] = hotel
    context["feedbacks"] = Feedback.objects.all()
    return render(request, "feedback.html", context)


class ThisFeedback(DetailView):
    model = Feedback
    template_name = 'feed.html'


def add_feedback(request, hotel):
    context = {}
    form = addFeedback(request.POST or None, hotel, request.user.id)
    context['form'] = form
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/mainn/')
    return render(request, 'add_feed.html', context)


def add_reserve(request, room):
    context = {}
    form = addReserve(request.POST or None)
    context['form'] = form
    if form.is_valid():
        reserve = form.save(commit=False)
        reserve.user = request.user
        reserve.hotel = list(Hotel.objects.filter(id=room))[0]
        reserve.save()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/mainn/')

    return render(request, 'add_reserve.html', context)

def myReserves(request):
    context = {}
    # add the dictionary during initialization
    context["userr"] = request.user
    context["reserves"] = Reserve.objects.all()

    return render(request, "reserves.html", context)


class ThisReserve(DetailView):
    model = Reserve
    template_name = 'this_reserve.html'


class EditReserve(UpdateView):
    model = Reserve
    fields = ['start_date', 'end_date']
    success_url = '/my_reserves/'
    template_name = 'reserve_update.html'


class DeleteReserve(DeleteView):
    model = Reserve
    template_name = 'reserve_delete_confirm.html'
    success_url = '/my_reserves/'


def guests(request, hotel):
    context = {}
    context["hotel"] = hotel
    context["reserves"] = Reserve.objects.all()
    now = datetime.now() - timedelta(days=30)
    context["now"] = now.strftime("%Y-%m-%d")
    print(now.strftime("%Y-%m-%d"))

    return render(request, "guests.html", context)


def panel(request):
    context = {}
    # add the dictionary during initialization
    context["reserves"] = Reserve.objects.all()

    return render(request, "panel_all.html", context)


def panel_compl(request):
    context = {}
    # add the dictionary during initialization
    context["reserves"] = Reserve.objects.all()

    return render(request, "panel_compl.html", context)


class EditPanel(UpdateView):
    model = Reserve
    fields = ['type']
    success_url = '/panel/'
    template_name = 'reserve_update.html'
