from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *


class IndexPageView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {'is_authenticated': request.user.is_authenticated})


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class RegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = '/profile'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/profile')
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class ToursListView(ListView):
    template_name = 'tours.html'
    model = Tour


class ReservationsListView(ListView):
    template_name = 'reservations.html'
    model = Reservation


class ReservationsByUserListView(LoginRequiredMixin, ListView):
    template_name = 'user_reservations.html'
    model = Reservation

    def get_queryset(self):
        user = self.request.user.pk
        return self.model.objects.filter(user=user)


class ReservationCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateReservationForm
    model = Reservation
    template_name = 'reservation_create.html'
    context_object_name = 'reservation'
    success_url = '/profile'

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial['user'] = self.request.user.pk
        initial['tour'] = get_object_or_404(Tour, pk=self.kwargs['pk'])
        return initial


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'
    context_object_name = 'reservation'
    success_url = '/profile'


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    fields = ['begin_date', 'end_date']
    template_name = 'reservation_update.html'
    context_object_name = 'reservation'
    success_url = '/profile'


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateCommentForm
    model = Comment
    template_name = 'comment.html'
    context_object_name = 'comment'
    success_url = '/tours'

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial['user'] = self.request.user.pk
        initial['tour'] = get_object_or_404(Tour, pk=self.kwargs['pk'])
        return initial


class CommentsListView(ListView):
    template_name = 'comments.html'
    model = Comment


class CommentsByTourListView(ListView):
    template_name = 'comments.html'
    model = Comment
    def get_queryset(self):
        return self.model.objects.filter(tour=self.kwargs['pk'])
