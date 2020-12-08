from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from .forms import *
from .models import *


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class HomeListView(ListView):
    model = Flight
    template_name = 'index.html'
    context_object_name = 'flights'


class HomeDetailViewFuture(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Flight
    template_name = 'detail.html'
    context_object_name = 'flight'
    form_class = PlaceForm
    success_msg = 'вы зарезервированны'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detailFuture_page', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.num_flight = self.get_object()
        self.object.passenger = self.request.user
        self.object.save()
        return super().form_valid(form)


def delete_comment(request, id):
    selected_comment = get_object_or_404(Place, id=id)
    if request.user == selected_comment.passenger:
        selected_comment.delete()
    return redirect('home')


class HomeDetailViewPast(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Flight
    template_name = 'detailPast.html'
    context_object_name = 'flight'

    form_class = CommentForm
    success_msg = 'Коммент опубликован!'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detailPast_page', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.flight = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class LastFlightView(ListView):
    model = Flight
    template_name = 'lastFlights.html'
    context_object_name = 'flights'


class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class MyprojectLogOutView(LogoutView):
    next_page = reverse_lazy('home')


class UserPage(ListView):
    model = User
    template_name = 'userPage.html'
    context_object_name = 'user'


class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')
    success_msg = 'Поользователь создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid
