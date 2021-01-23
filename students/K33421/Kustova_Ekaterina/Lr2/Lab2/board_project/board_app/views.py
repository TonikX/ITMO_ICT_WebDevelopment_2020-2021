from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
import datetime

from .forms import *
from .models import *
from django.contrib.auth import get_user_model


Participant = get_user_model()

def profile(request):
    context = {}
    context["dataset"] = Participant.objects.all()
    return render(request, 'profile.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'registration.html', context)



class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "main.html"
    success_url = "/profile/"

    def form_valid(self, form):
        self.participant = form.get_user()
        login(self.request, self.participant)
        return super(LoginFormView, self).form_valid(form)


def addrace(request):

    class RaceRegistration(CreateView):
        form_class = RaceRegistrationForm
        model = Race_Registration
        template_name = 'add_race_registration.html'
        context_object_name = 'registration'

        def get_initial(self):
            initial = super(RaceRegistration, self).get_initial()
            initial = initial.copy()
            initial['participant'] = self.request.participant.pk
            initial['race'] = get_object_or_404(Race, pk=self.kwargs['pk'])
            return initial

    return render(request, 'add_race_registration.html')

class Registrations(ListView):
    template_name = 'race_registrations.html'
    context_object_name = 'race_registrations.html'
    def get_queryset(self):
        self.participant = self.request.participant.pk
        return Race_Registration.objects.filter(participant=self.participant)



def races(request):
    context = {}
    context["dataset"] = Race.objects.all()
    return render(request,  "races.html", context)


def results(request):
    context = {}
    context["dataset"] = Win.objects.all()
    return render(request, 'results.html', context)


def forum(request):
    context = {}
    context["dataset"] = Comment.objects.all()

    form = CommentForm(request.POST)
    context['form'] = form

    if form.is_valid():
        object = form.save(commit=False)
        object.participant = request.participant
        object.date = datetime.datetime.now()
        object.save()
        return redirect('/forum/')
    return render(request, "forum.html", context)




