from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from datetime import datetime
from homework.models import Assignment, Student, Submission
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView

# Create your views here.


class IndexView(ListView):
    model = Assignment
    context_object_name = 'assignments'
    template_name = 'homework/index.html'

    def get_queryset(self):
        queryset = {
            'active_assignments': Assignment.objects.filter(is_active=True).order_by('-deadline'),
            'inactive_assignments': Assignment.objects.filter(is_active=False).order_by('-deadline')
        }
        return queryset


class LoginView(View):
    def post(self, request):
        # Attempt to sign user in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "homework/login.html", {
                "error": 'Invalid username and/or password.'
            })

    def get(self, request):
        return render(request, 'homework/login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class RegistrationView(View):
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        group_id = request.POST['group_id']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirm-password']
        if password != confirmation:
            return render(request, 'homework/register.html', {
                'error': 'Passwords must match.'
            })

        # Attempt to create new user
        try:
            user = Student.objects.create_user(
                username, email, password,
                first_name=first_name,
                last_name=last_name,
                group_id=group_id
            )
            user.save()
        except IntegrityError:
            return render(request, 'homework/register.html', {
                'error': 'Username already taken.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    def get(self, request):
        return render(request, 'homework/register.html')


class AssignmentDetailView(DetailView):
    model = Assignment


class SubmissionView(ListView):
    context_object_name = 'submissions'
    template_name = 'submission_list.html'

    def get_queryset(self):
        q = Submission.objects.filter(
            student=self.request.user).order_by('-date_of_submission')
        return q


class LeaderboardView(ListView):
    context_object_name = 'leaderboard'
    template_name = 'homework/leaderboard.html'

    def get_queryset(self):
        q = Submission.objects.order_by(
            '-grade')[:9]
        return q


@login_required
def AssignmentSubmission(request, assignment_id):
    if request.method == 'POST':
        try:
            assignment = Assignment.objects.get(pk=assignment_id)
        except Assignment.DoesNotExist:
            raise Http404('Assignment does not exist.')

        student = request.user
        solution = request.POST['answer']
        date_of_submission = datetime.now()

        sub = Submission.objects.create(
            assignment=assignment,
            student=student,
            solution=solution,
            date_of_submission=date_of_submission,
            grade=None,
            remarks=None
        )
        sub.save()
        return HttpResponseRedirect(reverse('index'))
