from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from MyApp.models import Hotel, ReservedRooms, Room, Client, Review
from django.views.generic.list import ListView
from datetime import date
from django.http import Http404
from .forms import RegistrationForm, BookForm, ReviewForm


class HotelsListView(ListView):
    model = Hotel
    template_name = 'index.html'


def hotel_view(request, hotel_id):
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404('Hotel does not exist')

    empty_rooms = []
    reserved_rooms = []
    last_clients = []
    for reservation in ReservedRooms.objects.all():
        if (date.today() - reservation.start_date).days < 30 and reservation.hotel_id == hotel:
            last_clients.append(reservation.client_id)
        if reservation.hotel_id == hotel:
            if reservation.start_date < date.today() and reservation.end_date > date.today():
                reserved_rooms.append(reservation.room_id)
            elif reservation.end_date == 'null':
                reserved_rooms.append(reservation.room_id)

    for room in Room.objects.all():
        if (room.hotel_id == hotel) and (room not in reserved_rooms):
            empty_rooms.append(room)

    return render(request, 'hotel.html', {
        'reserved_rooms': reserved_rooms,
        'empty_rooms': empty_rooms,
        'hotel': hotel,
        'last_clients': last_clients})


def room_view(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
        hotel = room.hotel_id
    except Room.DoesNotExist:
        raise Http404('Room does not exist')

    reviews = []
    for review in Review.objects.all():
        if review.room_id == room:
            reviews.append(review)

    return render(request, 'room.html', {'room': room, 'hotel': hotel, 'reviews': reviews})


def book_view(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise Http404('Room does not exist')

    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            for reservation in ReservedRooms.objects.all():
                if room == reservation.room_id:
                    if (reservation.start_date <= post.start_date and reservation.end_date >= post.end_date) or (reservation.end_date <= post.start_date and post.end_date >= reservation.end_date) or (form.start_date <= reservation.start_date and form.end_date >= reservation.start_date):
                        raise Http404("Room already reserved on this time")
            post.hotel_id = room.hotel_id
            post.room_id = room
            post.client_id = request.user
            post.save()
            return redirect('/')
        else:
            print(form.errors)
            print(request.user)
    else:
        form = BookForm()

    return render(request, 'book.html', {'room': room, 'form': form})


def review_view(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise Http404('Room does not exist')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.room_id = room
            post.client_id = request.user
            post.save()
            return redirect('/')
        else:
            print(form.errors)
            print(request.user)
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'room': room, 'form': form})


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
    return render(request, 'registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
