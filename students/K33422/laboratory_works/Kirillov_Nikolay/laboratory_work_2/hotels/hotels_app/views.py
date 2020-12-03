from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from hotels_app.models import *
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from hotels_app.forms import *
import datetime


# стартовая страница
def Index(request):
    template_name = 'index.html'
    return render(request, "index.html")


# вывод списка постояльцев за последний месяц
def HotelListView(request):
    today = datetime.date.today()
    today_year = today.year
    today_day = today.day
    last_month = today.month - 1 if today.month > 1 else 12
    month_ago = datetime.date(today_year, last_month, today_day)
    context = {}
    context["guests"] = Reservation.objects.all().order_by('room__hotel').filter(end_date__range=(month_ago, today))
    return render(request, "hotel_list.html", context)


# вывод списка пользователей
class UserListView(ListView):
    model = Client
    template_name = 'user_list_view.html'


# вывод списка комнат
class RoomListView(ListView):
    model = Room
    template_name = 'room_list_view.html'


'''
    class AddUser(CreateView):
    model = User
    template_name = 'add_user.html'
    fields = ['username', 'first_name', 'last_name', 'email']
'''


# вывод информации о комнате
def RoomView(request, pk):
    room = get_object_or_404(Room, id=pk)
    review = Review.objects.filter(room=pk)
    form = ReviewForm(request.POST or None)
    context = {"room": room, "reviews": review, "form": form}
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.room = room
        form.save()
        return redirect('room_view', pk)

    return render(request, "room_view.html", context)


# страница резервации
def ReservationView(request, pk):
    room = get_object_or_404(Room, id=pk)
    reservation = Reservation.objects.filter(room=pk)
    res_form = ReservationForm(request.POST or None)
    context = {"room": room, "reservation": reservation, "res_form": res_form}
    if res_form.is_valid():
        res_form = res_form.save(commit=False)
        res_form.owner = request.user
        res_form.room = room
        # room.is_reserved = True
        Room.objects.filter(id=pk).update(is_reserved=True)
        res_form.save()
    return render(request, "reservation.html", context)


# сраница удаления
def ResDelete(request, pk):
    query = get_object_or_404(Reservation, room_id=pk)
    owner = query.owner.username
    start_date = query.start_date
    user_now = request.user.username
    today = datetime.date.today()
    if str(owner) == str(user_now):
        if start_date < today:
            return HttpResponse('You cannot delete reservations that have passed')
        else:
            query.delete()
            Room.objects.filter(id=pk).update(is_reserved=False)
            return render(request, "res_delete.html")
    return HttpResponse('Not your reservation or ')
