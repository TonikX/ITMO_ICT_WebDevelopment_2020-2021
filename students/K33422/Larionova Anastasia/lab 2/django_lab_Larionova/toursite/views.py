from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .form import *
from .models import *
from django.contrib.auth import authenticate, login


def main(request):
    return render(request, 'main.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/profile')

    else:
        form = RegistrationForm()

    visual = {'form': form}
    return render(request, 'registration/register.html', visual)


def tourslist(request):
    visual = {"tours": Tour.objects.all()}
    return render(request, 'tours.html', visual)


class CreateReserve(CreateView):
    form_class = CreateReserveForm
    model = Reserve
    template_name = 'reserve.html'
    context_object_name = 'reserve'
    success_url = '/profile'
    
    def get_initial(self):
        initial = super(CreateReserve, self).get_initial()
        initial = initial.copy()
        initial['username'] = self.request.user.pk
        initial['name'] = get_object_or_404(Tour, pk=self.kwargs['pk'])
        return initial


def soldtourslist(request):
    visual = {"reserves": Reserve.objects.all()}
    return render(request, 'soldtours.html', visual)


class CreateReview(CreateView):
    form_class = CreateReviewForm
    model = Review
    template_name = 'review.html'
    context_object_name = 'review'
    success_url = '/reviews'

    def get_initial(self):
        initial = super(CreateReview, self).get_initial()
        initial = initial.copy()
        initial['username'] = self.request.user.pk
        return initial


def reviewslist(request):
    visual = {"reviews": Review.objects.all()}
    return render(request, 'reviews.html', visual)


class listreserves(ListView):
    template_name = 'myreserves.html'
    context_object_name = 'reserves_list'

    def get_queryset(self):
        self.user = self.request.user.pk
        return Reserve.objects.filter(username=self.user)


class deletereserveView(DeleteView):
    model = Reserve
    template_name = 'deletereserve.html'
    context_object_name = 'reserve'
    success_url = '/profile'


class updatereserveView(UpdateView):
    model = Reserve
    fields = ['start_date', 'end_date']
    template_name = 'updatereserve.html'
    context_object_name = 'reserve'
    success_url = '/profile'