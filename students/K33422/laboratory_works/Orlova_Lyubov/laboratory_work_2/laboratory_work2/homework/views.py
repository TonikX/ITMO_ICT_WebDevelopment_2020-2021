from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from .models import *
from .forms import *


def register_page(request):

    if request.user.is_authenticated:
        return redirect('/tasks_list/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'registration/register.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('/tasks_list/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/tasks_list/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'registration/login.html', context)


def logoutUser(request):

    logout(request)
    return redirect('login')


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
        initial['student_subm'] = self.request.user.id
        initial['task_subm'] = get_object_or_404(Task, pk=self.kwargs['pk'])
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
