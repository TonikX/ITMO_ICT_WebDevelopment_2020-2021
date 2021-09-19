from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AddCommentForm, EditReservationForm, ReservateRoomForm, AuthUserForm
from django.views.generic.base import View
from .models import Comentator, Comment, Hotel, HotelRoom, RoomReservation, UserRoom
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')


class RegisterFormView(FormView):
    model = get_user_model()
    form_class = UserCreationForm

    success_url = "/accounts/login/"

    template_name = "register.html"

    def form_valid(self, form):
        user = form.save()
        Comentator.objects.create(user=user, rating=0)

        return super(RegisterFormView, self).form_valid(form)


class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class MyLogOutView(LogoutView):
    next_page = reverse_lazy('home')


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel_list.html'
    context_object_name = 'hotel'


class HotelDetailView(View):
    def get(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        rooms = hotel.rooms.all()

        return render(request, 'hotel.html', {'hotel': hotel, 'rooms': rooms})


class RoomDetailView(View):
    def get(self, request, pk):
        room = HotelRoom.objects.get(pk=pk)
        conveniences = room.conveniences.all()
        history = room.room_history.all()
        can_add_comment = False
        comments = Comment.objects.filter(accommodation__in=history).all()

        for h in history:
            print("history")
            print(history)
            print(h)
            if h.user == request.user:
                can_add_comment = True
                break

        return render(request, 'room.html', {
            'room': room,
            'conveniences': conveniences,
            'history': history,
            'can_add_comment': can_add_comment,
            'comments': comments,
        })


class ProfileView(View):
    def get(self, request):
        reservations = request.user.reservations.all()
        history = request.user.user_history.all()
        user = request.user
        return render(request, 'profile.html', {'reservations': reservations, 'history': history, 'user': user})


class ReservateRoomView(View):
    def get(self, request, pk):
        return render(request, 'reserve_room.html')

    def post(self, request, pk):
        form = ReservateRoomForm(request.POST)
        if form.is_valid():
            begin_date = form.cleaned_data['begin_date']
            end_date = form.cleaned_data['end_date']
            RoomReservation.objects.create(
                room=HotelRoom.objects.get(pk=pk),
                begin_date=begin_date,
                end_date=end_date,
                user=request.user
            )

            return HttpResponseRedirect('/room/{}/'.format(pk))


class EditReservationView(View):
    def get(self, requset, pk):
        reservation = RoomReservation.objects.get(pk=pk)

        return render(requset, 'edit_reservation.html', {'reservation': reservation})

    def post(self, requset, pk):
        reservation = RoomReservation.objects.get(pk=pk)
        form = EditReservationForm(requset.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile')

        print(form.errors)
        return HttpResponseBadRequest()


class DeleteReservationView(View):
    def get(self, requset, pk):
        reservation = RoomReservation.objects.get(pk=pk)
        reservation.delete()
        return HttpResponseRedirect("/accounts/profile")


class AddCommentView(View):
    def get(self, request, pk):
        room = HotelRoom.objects.get(pk=pk)
        try:
            user_room_history = UserRoom.objects.filter(user=request.user, room=room).all()
            return render(request, 'add_comment.html', {'accommodations': user_room_history})
        except UserRoom.DoesNotExist:
            return redirect('/')

    def post(self, request, pk):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user=request.user,
                accommodation=form.cleaned_data['accommodation'],
                text=form.cleaned_data['text']
            )

            return HttpResponseRedirect('/room/{}/'.format(pk))
        print(form.errors)
        return HttpResponseBadRequest()


class UserRoomListView(ListView):
    model = UserRoom
    template_name = 'userroom_list.html'
    context_object_name = 'object_list'
