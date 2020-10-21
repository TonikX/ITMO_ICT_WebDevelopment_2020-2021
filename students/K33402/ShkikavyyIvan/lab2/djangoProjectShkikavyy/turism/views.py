from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .form import *
from .models import *
from django.contrib.auth import authenticate, login


def main(request):
    return render(request, 'main.html')


def lc(request):
    return render(request, 'lc.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/lc')
    else:
        form = RegistrationForm()
    visual = {'form': form}
    return render(request, 'registration/signin.html', visual)


class CreateReservation(CreateView):
    form_class = CreateReservationForm
    model = Reservation
    template_name = 'reservation.html'
    context_object_name = 'reservation'
    success_url = '/lc'

    def get_initial(self):
        initial = super(CreateReservation, self).get_initial()
        initial = initial.copy()
        initial['username'] = self.request.user.pk
        initial['nameoftour'] = get_object_or_404(Tour, pk=self.kwargs['pk'])
        return initial


class UpdateReserveView(UpdateView):
    model = Reservation
    fields = ['begin_date', 'end_date']
    template_name = 'upreservation.html'
    context_object_name = 'reservation'
    success_url = '/lc'


class DeleteReserveView(DeleteView):
    model = Reservation
    template_name = 'delreservation.html'
    context_object_name = 'reservation'
    success_url = '/lc'


def reservedtourlist(request):
    visual = {"reservations": Reservation.objects.all()}
    return render(request, 'reservedtour.html', visual)

class listreservations(ListView):
    template_name = 'lcreservations.html'
    context_object_name = 'reservation_list'
    def get_queryset(self):
        self.user = self.request.user.pk
        return Reservation.objects.filter(username=self.user)

def commentlist(request):
    visual = {"comments": Comment.objects.all()}
    return render(request, 'comments.html', visual)

def tourlist(request):
    visual = {"tours": Tour.objects.all()}
    return render(request, 'tour.html', visual)

class CreateComment(CreateView):
    form_class = CreateCommentForm
    model = Comment
    template_name = 'comment.html'
    context_object_name = 'comment'
    success_url = '/commentlist'
    def get_initial(self):
        initial = super(CreateComment, self).get_initial()
        initial = initial.copy()
        initial['commentator'] = self.request.user.pk
        return initial
