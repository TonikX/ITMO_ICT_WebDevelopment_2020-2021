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


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/homeworks/')
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
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/homeworks/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/homeworks/')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


class HomeworksList(ListView):
    model = Homework
    template_name = 'homeworks.html'
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


class HomeworkDetail(DetailView):
    model = Homework
    template_name = "homework_detail.html"


class AnswersList(ListView):
    model = Answer
    template_name = 'answers.html'
    def get_queryset(self):
        return Answer.objects.all()


class AddAnswer(CreateView):
    form_class = AddAnswerForm
    model = Answer
    template_name = 'add_answer.html'
    def get_initial(self):
        initial = super(AddAnswer, self).get_initial()
        initial = initial.copy()
        initial['student'] = self.request.user.id
        initial['homework'] = get_object_or_404(Homework, pk=self.kwargs['pk'])
        return initial


class AnswerUpdate(UpdateView):
    model = Answer
    fields = ['answer']
    template_name = 'update_answer.html'


class AnswerDelete(DeleteView):
    model = Answer
    template_name = 'delete_answer.html'


class GradesTable(ListView):
    model = Answer
    template_name = 'grades_table.html'
    def get_queryset(self):
        return Answer.objects.all()