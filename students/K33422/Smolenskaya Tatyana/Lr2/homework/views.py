from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import *
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render, get_object_or_404


class HomePageView(TemplateView):
    template_name = 'home.html'


def profile(request):
    return render(request, 'profile.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile/')

    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('/')


class TasksList(ListView):
    model = Task
    template_name = 'task_list.html'
    queryset = model.objects.all()

    def get_queryset(self):
        task = self.request.GET.get('task')
        if task:
            try:
                task = int(task)
                queryset = self.queryset.filter(task=task)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.queryset


class TaskDescription(DetailView):
    model = Task
    template_name = "task_view.html"


class CompletedTask(ListView):
    model = Submission
    template_name = 'completed_list.html'

    def get_queryset(self):
        return Submission.objects.all()


class AddSubmission(CreateView):
    form_class = AddSubmissionForm
    model = Submission
    template_name = 'add_submission.html'

    def get_initial(self):
        initial = super(AddSubmission, self).get_initial()
        initial = initial.copy()
        initial['student'] = self.request.user.id
        initial['task'] = get_object_or_404(Task, pk=self.kwargs['pk'])
        return initial


class SubmissionUpdate(UpdateView):
    model = Submission
    fields = ['submission']
    template_name = 'update_submission.html'


class SubmissionDelete(DeleteView):
    model = Submission
    template_name = 'delete_submission.html'


class GradesTable(ListView):
    model = Submission
    template_name = 'grades_list.html'

    def get_queryset(self):
        return Submission.objects.all()