from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import  MemberForm, TeamForm
from .models import Team, Task, Solution
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView


def registration(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = MemberForm()
    return render(request, 'hackathon/registration.html', {'form': form})


def team(request):
    if request.method == 'POST':
        try:
            team = Team.objects.get(captain=request.user.id)
            form = TeamForm(request.POST, instance=team)
        except:
            form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/team')
    else:
        team = Team.objects.get(captain=request.user.id)
        form = TeamForm(instance=team)
    return render(request, 'hackathon/team.html', {'form': form})


def profile(request):
    form = TeamForm()
    return render(request, 'hackathon/profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


class TasksView(ListView):
    model = Task

    def get_context_data(self,**kwargs):
        context = super(TasksView,self).get_context_data(**kwargs)
        # context['team'] = Team.objects.get(captain=self.request.user)
        return context


class SolutionCreateView(CreateView):
    model = Solution
    fields = ["text"]

    def get_success_url(self):
        #return reverse('book-detail', kwargs={'pk': self.object.pk})
        return "/tasks"

    def form_valid(self, form):
        form.instance.task = Task.objects.get(pk=self.kwargs["pk"])
        form.instance.team_id = Team.objects.get(captain=self.request.user.id).pk
        return super(SolutionCreateView, self).form_valid(form)


class SolutionUpdateView(UpdateView):
    model = Solution
    fields = ["text"]


class TaskCreateView(CreateView):
    model = Task
    fields = ["text", "upload"]

    def get_success_url(self):
        return "/tasks"


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["text", "upload"]

    def get_success_url(self):
        return "/tasks"