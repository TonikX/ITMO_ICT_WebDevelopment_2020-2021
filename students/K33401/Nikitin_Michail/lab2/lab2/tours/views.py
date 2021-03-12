from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import RegistrationForm, CommentForm


class StartPage(ListView):
    model = Tour
    template_name = 'index.html'


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    visual = {'form': form}
    return render(request, 'registration.html', visual)


def tour_view(request, tour_id):
    try:
        tour = Tour.objects.get(pk=tour_id)
    except Tour.DoesNotExist:
        raise Http404("such Tour doesn't exist")
    return render(request, 'tour_page.html', {"tour": tour})


def booking(request, tour_id):
    try:
        tour = Tour.objects.get(pk=tour_id)
    except Tour.DoesNotExist:
        raise Http404("such Tour doesn't exist")
    Booked.objects.create(
        tour=tour,
        user=request.user,
        )
    tour.count_of_booked += 1
    tour.save()
    return render(request, 'tour_booking.html', {"name": tour.name})


class BookList(ListView):
    model = Booked
    template_name = 'booked_list.html'


def booking_del(request, book_id):
    try:
        book = Booked.objects.get(pk=book_id)
        tour = Tour.objects.get(pk=book.tour.id)
    except Booked.DoesNotExist:
        raise Http404('no Such Book')
    book.delete()
    tour.count_of_booked -= 1
    tour.save()
    return redirect('/')

'''
class RetryCommenting(CreateView):
    model = UsersComments
    template_name = 'working_comments.html'
    fields = ['text', 'rate']
    success_url = '/'

    #def form_valid(self, form):
     #   commenting_user = self.request.user

'''
def users_comment(request, tour_id):
    try:
        tour = Tour.objects.get(pk=tour_id)
    except Tour.DoesNotExist:
        raise Http404("such Tour doesn't exist")
    form = CommentForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.commented_tour = tour
        post.commenting_user = request.user
        form = post
        form.save()
    else:
        print(form.errors)
        print(request.user)
        form = CommentForm
    return 3#render(request, 'working_comments.html', {"form": form})


class CommentList(ListView):
    model = UsersComments
    template_name = 'all_comments.html'