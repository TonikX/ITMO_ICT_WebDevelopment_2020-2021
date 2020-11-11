from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import GuestForm, BookingForm, ReviewForm
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Booking, Hotel, Review, Guest
import datetime
import dateutil.relativedelta

def table(request):
    d2 = datetime.datetime.now() - datetime.timedelta(days=30)
    guests = Guest.objects.filter(
        booking__start__lt=datetime.datetime.now(),
        booking__start__gt=d2,
    )
    return render(request, 'hotel/guest_list.html', {'guests': guests})

def guest_registration(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/booking')
    else:
        form = GuestForm()
    return render(request, 'hotel/registration.html', {'form': form})

class BookingView(ListView):
    model = Booking

    def get_context_data(self, **kwargs):
        context = super(BookingView, self).get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()
        context['booking_form'] = BookingForm
        if self.request.user.is_authenticated:
            context['bookings'] = Booking.objects.filter(guest=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        # form.guest = request.user.id
        if form.is_valid():
            print(form)
            booking = form.save(commit=False)
            booking.guest = request.user
            booking.save()
        else:
            print(form.errors)
            print(request.user)
        return redirect('/booking')

class BookingDelete(DeleteView):
    model = Booking
    success_url = "/booking"

class BookingSave(UpdateView):
    model = Booking
    fields = [
        "hotel",
        "room",
        "start",
        "end",
    ]
    success_url = "/booking"

#class BookingEdit(TemplateView):
#    model = Booking

def logout_view(request):
    logout(request)
    return redirect('/booking')

class ReviewView(CreateView):
    model = Review
    fields = [
        "booking",
        "text",
        "rating",
    ]
    success_url = "/booking"

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        context['booking_id'] = int(self.kwargs.get("booking_id", 0))
        context['form'] = ReviewForm
        context['booking'] = Booking.objects.get(id=context['booking_id'])
        return context