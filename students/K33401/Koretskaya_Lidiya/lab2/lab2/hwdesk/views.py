from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import *
from .models import *
from datetime import datetime
from django.urls import reverse_lazy

class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    template_name = "register.html"

    model = CustomUser
    success_url = "/login"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"

    model = CustomUser

    success_url = "/profile"

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginFormView, self).form_valid(form)

def loginPass(request):
    if request.user.type == 'teacher':
        return render(request, 'Teacher.html')
    else:
         return render(request, 'Pupil.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login")

class IndexView(TemplateView):
  template_name = "index.html"

#Teacher actions
class TeacherTask(ListView):
    model = Task
    template_name = 'TeacherTask.html'
    success_url = '/task'


class TeacherTaskCreate(CreateView):
    form_class = AddTaskTeacher
    model = Task
    #fields = ['class_name', 'subject', 'deadline', 'task_text', 'fines_info',]
    template_name = 'TeacherTask_form.html'
    success_url = '/task'

    def form_valid(self, form):
        now = datetime.now()
        form.instance.date_of_publication = now.strftime("%Y-%m-%d")
        first = self.request.user.first_name
        last = self.request.user.last_name
        teacher = Teacher.objects.filter(first_name=first, last_name=last)
        form.instance.teacher = teacher.first()
        return super(TeacherTaskCreate, self).form_valid(form)

class TeacherTaskDetail(DetailView):
    model = Task
    template_name = 'TeacherTask_detail.html'

    def get_context_data(self, *args, **kwargs):
        id = self.kwargs['pk']
        task = get_object_or_404(Task, pk=id)
        checks = CheckTask.objects.filter(task=task)
        check_id = []
        for check in checks:
            check_id.append(check.task.id)

        context = super(TeacherTaskDetail, self).get_context_data()
        context['new_tasks'] = LoadTask.objects.exclude(task_id__in=check_id).filter(task=task)
        return context

class TeacherTaskUpdate(UpdateView):
    model = Task
    fields = ['class_name', 'subject', 'teacher', 'date_of_publication',
              'deadline', 'task_text', 'fines_info', ]
    template_name = 'TeacherTask_form.html'
    success_url = '/task'

class TeacherTaskDelete(DeleteView):
    model = Task
    template_name = 'TeacherTask_delete.html'
    success_url = '/task'

class TeacherTaskCheck(CreateView):
    form_class = CheckTaskTeacher
    model = CheckTask
    template_name = 'TeacherTask_check.html'
    def form_valid(self, form):
        id = self.kwargs['pk']
        task = get_object_or_404(Task, pk=id)
        pupil = self.kwargs['ppk'].split(' ')
        pupil = get_object_or_404(Pupil, first_name=pupil[0], last_name=pupil[1])
        form.instance.task = task
        form.instance.pupil = pupil
        return super(TeacherTaskCheck, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('teacher_detail', kwargs={'pk': self.kwargs['pk']})




#Pupil actions
class PupilTask(ListView):
    model = Pupil
    template_name = 'PupilTask.html'
    success_url = '/pupil_task'
    context_object_name = 'pupils'

    def get_context_data(self, *args, **kwargs):
        first = self.request.user.first_name
        last = self.request.user.last_name
        pupil = get_object_or_404(Pupil, first_name=first, last_name=last)
        class_ = pupil.class_name
        loads = LoadTask.objects.filter(pupil = pupil).all()
        load_id = []
        for load in loads:
            load_id.append(load.task.id)
        context = super(PupilTask, self).get_context_data()
        context['new_tasks'] = Task.objects.exclude(id__in = load_id).filter(class_name=class_)
        context['done_tasks'] = Task.objects.filter(id__in = load_id).filter(class_name=class_)
        return context

class PupilTask_detail(DetailView):
    model = Task
    template_name = 'PupilTask_detail.html'
    success_url = '/pupil_task/<int:pk>'

class PupilMark(ListView):
    model = Pupil
    template_name = 'PupilMark.html'
    success_url = '/marks'

    def get_context_data(self, *args, **kwargs):
        first = self.request.user.first_name
        last = self.request.user.last_name
        pupil = get_object_or_404(Pupil, first_name=first, last_name=last)
        class_ = pupil.class_name
        classmates = Pupil.objects.filter(class_name=class_)
        context = super(PupilMark, self).get_context_data()
        context['classmates'] = Pupil.objects.filter(class_name=class_)
        context['checks'] = CheckTask.objects.filter(pupil_id__in=classmates)
        return context

class PupilTask_create(CreateView):
    form_class = LoadTaskPupil
    model = LoadTask
    #fields = ['pupil', 'task', 'decision',]
    template_name = 'PupilTask_form.html'
    success_url = '/pupil_task'

    def form_valid(self, form):
        now = datetime.now()
        #form.instance.date_of_publication = now.strftime("%Y-%m-%d")
        first = self.request.user.first_name
        last = self.request.user.last_name
        pupil = Pupil.objects.filter(first_name=first, last_name=last)
        id = self.kwargs['pk']
        task = get_object_or_404(Task, pk=id)
        form.instance.pupil = pupil.first()
        form.instance.task = task
        return super(PupilTask_create, self).form_valid(form)

















