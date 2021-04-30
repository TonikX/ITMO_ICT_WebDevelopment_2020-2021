from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from datetime import date as d_date

from .models import *
from .forms import *


def redirect_board(request):
    print('redirect')
    return redirect('flight_list_url', permanent=False)


def signoff(request):
    logout(request)
    return redirect_board(request)


def signin(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'board/sign.html', context={'form': form, 'page_type': 'Sign in'})
    # https://docs.djangoproject.com/en/3.1/topics/auth/default/#how-to-log-a-user-in
    username = request.POST['username']
    password = request.POST['password']
    bound_form = UserLoginForm(request.POST)
    user = authenticate(request, username=username, password=password)
    if not User.objects.filter(username=username):
        bound_form.add_error(
            'username', 'A user with that username does not exist')
    if user is not None:
        login(request, user)
        return redirect_board(request)
    return render(request, 'board/sign.html', context={'form': bound_form, 'page_type': 'Sign in'})


class UserCreate(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'board/sign.html', context={'form': form, 'page_type': 'Sign up'})

    def post(self, request):
        bound_form = UserForm(request.POST)
        if bound_form.is_valid():
            new_user = bound_form.save()

            #############################
            login(request, new_user)
            return redirect_board(request)
            # return signin(request)
        return render(request, 'board/sign.html', context={'form': bound_form, 'page_type': 'Sign up'})


class CommentCreate(LoginRequiredMixin, View):
    login_url = '/sign_in/'
    redirect_field_name = None

    def get(self, request, number):
        form = CommentCreateForm()
        flight = Flight.objects.get(number=number)
        reservation = Reservation.objects.filter(
            passenger=request.user, flight=flight, ticket_number__isnull=False)
        if reservation.count() > 1:
            reservation = reservation[1]
        return render(request, 'board/make_comment.html', context={'form': form, 'flight': flight, 'user': request.user, 'flight_date': reservation.values('date')})

    def post(self, request, number):
        bound_form = CommentCreateForm(request.POST)
        flight = Flight.objects.get(number=number)
        reservation = Reservation.objects.filter(
            passenger=request.user, flight=flight, ticket_number__isnull=False)
        if reservation.count() > 1:
            reservation = reservation[1]
        print()
        print(bound_form)
        print()
        if bound_form.is_valid():
            if int(bound_form.cleaned_data['rating']) > 10:
                bound_form.add_error(
                    'rating', 'Please ensure that the rating is a number from 1 to 10')
                return render(request, 'board/make_comment.html', context={'form': bound_form, 'flight': flight, 'user': request.user, 'flight_date': reservation.values('date')})
            bound_form.save()
            return redirect(flight.get_absolute_url())
        return render(request, 'board/make_comment.html', context={'form': bound_form, 'flight': flight, 'user': request.user, 'flight_date': reservation.values('date')})


class FlightList(View):

    def get(self, request):
        # departures
        deps = Flight.objects.filter(is_departure=True)
        arrs = Flight.objects.filter(is_departure=False)
        return render(request, 'board/flight_list.html', context={'deps': deps, 'arrs': arrs})


class FlightDetail(View):
    # в шаблонах не сделать обычные циклы по range(1,4) или даже по листу [1,2,3]
    stars = [i for i in range(1, 11)]

    def get(self, request, number):
        try:
            flight = Flight.objects.get(number=number)
            comments = Comment.objects.filter(flight=flight.id)
        except ObjectDoesNotExist:
            return redirect_board(request)
        if flight.is_departure:
            can_comment = True if request.user.is_authenticated and Reservation.objects.filter(
                passenger=request.user, flight=flight, ticket_number__isnull=False).count() else False
            return render(request, 'board/flight_detail.html', context={'flight': flight, 'comments': comments, 'can_comment': can_comment, 'stars': self.stars})
        return redirect_board(request)


class PassengerList(LoginRequiredMixin, View):
    login_url = '/sign_in/'
    redirect_field_name = None

    def get(self, request, number):
        try:
            flight = Flight.objects.get(number=number)
        except ObjectDoesNotExist:
            print('errrrr')
            return redirect_board(request)
        passengers = flight.passengers.all().distinct()
        print()
        print(flight.passengers)
        print()
        print(flight)
        print()
        return render(request, 'board/passenger_list.html', context={'flight': flight, 'passengers': passengers})


class ReservationList(LoginRequiredMixin, View):
    login_url = '/sign_in/'
    redirect_field_name = None

    def get(self, request):
        reservations = Reservation.objects.filter(passenger_id=request.user.id)
        return render(request, 'board/reservation_list.html', context={'reservations': reservations})

    def post(self, request):
        reservation = request.POST['reservation']
        try:
            res = Reservation.objects.get(id=reservation)
            res.delete()
        except ObjectDoesNotExist:
            return redirect_board(request)
        reservations = Reservation.objects.filter(passenger_id=request.user.id)
        return render(request, 'board/reservation_list.html', context={'reservations': reservations})


class ReservationEdit(LoginRequiredMixin, UpdateView):
    login_url = '/sign_in/'
    redirect_field_name = None
    model = Reservation
    form_class = ReservationEditForm
    template_name = 'board/edit_reservation.html'
    context_object_name = 'reservation'
    # fields = ['seat', 'date']
    success_url = '/my_reservations/'

    seats = [[{'seat_number': str(i)+s}
              for s in ['a', 'b', 'c', 'd']] for i in range(1, 10)]


class ReservationCreate(LoginRequiredMixin, View):

    login_url = '/sign_in/'
    redirect_field_name = None

    seats = [[{'seat_number': str(i)+s}
              for s in ['a', 'b', 'c', 'd']] for i in range(1, 10)]

    def get(self, request, number):
        form = ReservationForm()
        try:
            flight = Flight.objects.get(number=number)
        except ObjectDoesNotExist:
            return redirect_board(request)
        if not flight.is_departure:
            return redirect_board(request)
        return render(request, 'board/create_reservation.html', context={'form': form, 'flight': flight, 'seats': self.seats})

    def post(self, request, number):

        bound_form = ReservationForm(request.POST)

        flight = Flight.objects.get(number=number)

        date = bound_form['date'].value()
        seat = bound_form['seat'].value()
        [year, month, day] = list(
            map(lambda x: int(x), date.split('-')))
        # немного условий
        if (d_date(year, month, day) - d_date.today()).days not in range(1, 15):
            bound_form.add_error(
                'date', 'You can only reserve a flight from tomorrow to 2 weeks later')
        if Reservation.objects.filter(date=date, passenger=bound_form['passenger'].value(), flight=bound_form['flight'].value(), seat=seat).count():
            bound_form.add_error(
                'seat', ' {} - this seat is not free, choose another one'.format(seat))
        print(bound_form.is_valid())
        if bound_form.is_valid():
            bound_form.save()
            return render(request, 'board/create_reservation.html', context={'form': bound_form, 'flight': flight, 'seats': self.seats})
        return render(request, 'board/create_reservation.html', context={'form': bound_form, 'flight': flight, 'seats': self.seats})
