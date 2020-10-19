from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView, TemplateView, ListView, DetailView, CreateView, UpdateView

from racing_scoreboard.forms import RegisterForm, AddCommentForm, CreateRacerForm
from racing_scoreboard.models import Race, Comment, Racer, RaceRacer

User = get_user_model()


# Регистрация пользователя
def register(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "register_form": register_form
    }

    if register_form.is_valid():
        username = register_form.cleaned_data.get("username")
        first_name = register_form.cleaned_data.get("first_name")
        last_name = register_form.cleaned_data.get("last_name")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")

        User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)

        return redirect('/login/')

    return render(request, "registration/register.html", context)


# Вывод информации об автогонках (плюс регистрация и удаление регистрации на гонку)
class RaceListView(ListView):
    template_name = 'main.html'
    model = Race

    def get_queryset(self):
        register_id = self.request.GET.get('register_id')
        delete_id = self.request.GET.get('delete_id')

        if register_id:
            try:
                register_id = int(register_id)
                RaceRacer.objects.create(race_id=register_id, racer_id=self.request.user.racer.id)

            except:
                pass

        if delete_id:
            try:
                delete_id = int(delete_id)
                RaceRacer.objects.get(race_id=delete_id, racer_id=self.request.user.racer.id).delete()

            except:
                pass

        return Race.objects.all()


# Детали гонки
class RaceDetailView(DetailView, CreateView):
    template_name = 'race_detail.html'
    model = Race
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse('race-detail', args=[str(self.kwargs.get('pk'))])

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.commentator = self.request.user
        comment.race_id = self.kwargs.get('pk')

        return super(RaceDetailView, self).form_valid(form)


# Детали о гонщике
class RacerDetailView(DetailView):
    template_name = 'racer_detail.html'
    model = Racer


# Создание гонщика
class RacerCreateView(CreateView):
    template_name = 'racer_create.html'
    model = Racer
    form_class = CreateRacerForm

    def get_success_url(self):
        return reverse('racer-detail', args=[str(self.object.id)])

    def form_valid(self, form):
        racer = form.save(commit=False)
        racer.user_info = self.request.user

        return super(RacerCreateView, self).form_valid(form)


# Обновление гонщика
class RacerUpdateView(UpdateView):
    model = Racer
    template_name = 'racer_create.html'
    form_class = CreateRacerForm

    def get_success_url(self):
        return reverse('racer-detail', args=[str(self.object.id)])


# Мои регистрации
class RegistrationListView(ListView):
    model = RaceRacer
    template_name = 'registration.html'

    def get_queryset(self):
        delete_id = self.request.GET.get('delete_id')

        if delete_id:
            try:
                delete_id = int(delete_id)
                RaceRacer.objects.get(race_id=delete_id, racer_id=self.request.user.racer.id).delete()

            except:
                pass

        return RaceRacer.objects.filter(racer_id=self.request.user.racer.id)
