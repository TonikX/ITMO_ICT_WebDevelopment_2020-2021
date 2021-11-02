from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .models import Booking, Schedule, Comments
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .forms import LoginForm, UserRegistrationForm, CommentForm, ReverseForm


# Create your views here.
def post(request):
    info = Schedule.objects.all()
    return render(request, 'airTravel/index.html', context={'info': info})


# регистрация пассажиров
def index(request, id):
    try:
        plane = Schedule.objects.get(id=id)
        bookings = Booking.objects.filter(plane=id, moderation=True)
        if request.method == "POST":
            rev = ReverseForm(request.POST)
            if rev.is_valid():
                rev = rev.save(commit=False)
                rev.name = request.POST.get("name")
                rev.surname = request.POST.get("surname")
                rev.place = request.POST.get("place")
                rev.plane = plane
                rev.user = request.user
                rev.save()
                url = f'/reserve/{str(id)}'
                return HttpResponseRedirect(url)
        else:
            value = ['A01', 'A02', 'A03', 'A04', 'B01', 'B02', 'B03', 'B04', 'C01', 'C02', 'C03', 'C04',
                     'D01', 'D02', 'D03', 'D04']
            rev = ReverseForm()
            posts = Booking.objects.filter(plane=id)
            p = []
            for post in posts:
                p.append(post.place)
            for j in p:
                for i in range(len(value) - 1):
                    if j == value[i]:
                        del value[i]

            return render(request, "airTravel/form.html", {"plane": plane,
                                                           "bookings": bookings,
                                                           "rev": rev,
                                                           "value": value})
    except Booking.DoesNotExist:
        return HttpResponseNotFound("<h2>Comments not found</h2>")


# изменение данных в бд
def edit(request, pk, id):
    try:
        page = Schedule.objects.get(id=id)
        booking = Booking.objects.get(id=pk)

        if request.method == "POST":
            booking.name = request.POST.get("name")
            booking.surname = request.POST.get("surname")
            booking.place = request.POST.get("place")
            booking.save()
            url = f'/reserve/{str(id)}'
            return HttpResponseRedirect(url)
        else:
            return render(request, "airTravel/edit.html", {"booking": booking})
    except Booking.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, pk, id):
    try:
        page = Schedule.objects.get(id=id)
        booking = Booking.objects.get(id=pk)
        booking.delete()
        url = f'/reserve/{str(id)}'
        return HttpResponseRedirect(url)
    except Booking.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# Функция регистрации
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'airTravel/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'airTravel/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'airTravel/register.html', {'user_form': user_form})


# комментарии
def comments(request, id):
    try:
        flight = Schedule.objects.get(id=id)
        comments = Comments.objects.filter(flight=id)

        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.flight = flight
                form.save()
                url = f'/comments/{str(id)}'
                return HttpResponseRedirect(url)
        else:
            form = CommentForm()
            return render(request, "airTravel/comments.html", {"flight": flight,
                                                               "comments": comments,
                                                               "form": form})
    except Comments.DoesNotExist:
        return HttpResponseNotFound("<h2>Comments not found</h2>")
