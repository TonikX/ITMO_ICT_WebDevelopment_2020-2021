from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from main.forms import AddCommentForm, EditReservationForm, ReservateRoomForm
from django.views.generic.base import View
from main.models import Comentator, Comment, Hotel, HotelRoom, RoomReservation, UserRoom
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'main/index.html')


class RegisterFormView(FormView):
    model = get_user_model()
    form_class = UserCreationForm

    success_url = "/login/"

    template_name = "registration/register.html"

    def form_valid(self, form):
        user = form.save()
        Comentator.objects.create(user=user, rating = 0)

        return super(RegisterFormView, self).form_valid(form)


class HotelListView(ListView):
    model = Hotel


class HotelDetailView(View):
    def get(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        rooms = hotel.rooms.all()
        print("hotel:", pk)
        return render(request, 'main/hotel.html', {'hotel': hotel, 'rooms': rooms})


class RoomDetailView(View):
    def get(self, request, pk):
        room = HotelRoom.objects.get(pk=pk)
        conveniences = room.conveniences.all()
        history = room.room_history.all()
        can_add_comment = False
        comments = Comment.objects.filter(accommodation__in=history).all()

        for h in history:
            if (h.user == request.user):
                can_add_comment = True
                break

        return render(request, 'main/room.html', {
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
        return render(request, 'registration/profile.html', {'reservations': reservations, 'history': history})


class ReservateRoomView(View):
    def get(self, request, pk):
        return render(request, 'main/reserve_room.html')
    
    def post(self, request, pk):
        form = ReservateRoomForm(request.POST)
        if form.is_valid():
            begin_date = form.cleaned_data['begin_date']
            end_date = form.cleaned_data['end_date']
            RoomReservation.objects.create(
                room = HotelRoom.objects.get(pk=pk),
                begin_date=begin_date,
                end_date = end_date,
                user = request.user
            )

            return HttpResponseRedirect('/room/{}/'.format(pk))


class EditReservationView(View):
    def get(self, requset, pk):
        reservation = RoomReservation.objects.get(pk=pk)

        return render(requset, 'main/edit_reservation.html', {'reservation': reservation})
    
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
            return render(request, 'main/add_comment.html', {'accommodations': user_room_history})
        except UserRoom.DoesNotExist:
            return redirect('/')

    def post(self, request, pk):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user = request.user,
                accommodation = form.cleaned_data['accommodation'],
                text = form.cleaned_data['text']
            )

            return HttpResponseRedirect('/room/{}/'.format(pk))
        print(form.errors)
        return HttpResponseBadRequest()


class UserRoomListView(ListView):
    model = UserRoom

