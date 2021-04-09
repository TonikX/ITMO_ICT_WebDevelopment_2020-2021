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

class IndexView(TemplateView):
  template_name = "index.html"

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    model = CustomUser
    success_url = "/profile"
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginFormView, self).form_valid(form)
        
class TeacherRegisterFormView(FormView):
    form_class = TeacherCreationForm
    template_name = "register.html"
    model = CustomUser
    success_url = "/login/"
    def form_valid(self, form):
        form.save()
        return super(TeacherRegisterFormView, self).form_valid(form)

class StudentRegisterFormView(FormView):
    form_class = StudentCreationForm
    template_name = "register.html"
    model = CustomUser
    success_url = "/login/"
    def form_valid(self, form):
        form.save()
        return super(StudentRegisterFormView, self).form_valid(form)

def LoginPass(request):
    if request.user.role == 'teacher':
        return render(request, 'teacher.html')
    else:
         return render(request, 'student.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login/")


class AddHomework(CreateView):
    form_class = AddHomework
    model = Homework
    template_name = 'add_homework.html'
    success_url = '/homeworks/'
    def form_valid(self, form):
        name = self.request.user.name
        teacher = Teacher.objects.filter(name=name)
        print(teacher)
        form.instance.teacher = teacher.first()
        return super(AddHomework, self).form_valid(form)


class Homeworks(ListView):
    model = Homework
    template_name = 'homeworks.html'


class HomeworkDetail(DetailView):
    model = Homework
    template_name = 'homework.html'
    def get_context_data(self, *args, **kwargs):
        id = self.kwargs['pk']
        homework = get_object_or_404(Homework, pk=id)
        assignments = Assignment.objects.filter(homework=homework)
        ass_id = []
        for ass in assignments:
            ass_id.append(ass.homework.id)

        context = super(HomeworkDetail, self).get_context_data()
        context['new_tasks'] = Assignment.objects.filter(homework=homework)
        return context
        

class DeleteHomework(DeleteView):
    model = Homework
    template_name = 'delete_homework.html'
    success_url = '/homeworks/'


class AddAssessment(CreateView):
    form_class = AddAssessment
    model = Assessment
    template_name = 'add_assessment.html'
    success_url = '/homeworks/'
    def form_valid(self, form):
        id = self.kwargs['pk']
        homework = get_object_or_404(Homework, pk=id)
        student = self.kwargs['ppk']
        student = get_object_or_404(Student, pk=student)
        form.instance.homework = homework
        form.instance.student = student
        return super(AddAssessment, self).form_valid(form)


class ToDo(ListView):
    model = Student
    template_name = 'to_do.html'
    context_object_name = 'students'
    def get_context_data(self, *args, **kwargs):
        name = self.request.user.name
        student = get_object_or_404(Student, name=name)
        group = student.group_number
        assignments = Assignment.objects.filter(student=student).all()
        ass_id = []
        for assignment in assignments:
            ass_id.append(assignment.homework.id)
        context = super(ToDo, self).get_context_data()
        context['new_tasks'] = Homework.objects.exclude(id__in = ass_id).filter(group_number=group)
        context['done_tasks'] = Homework.objects.filter(id__in = ass_id).filter(group_number=group)
        return context


class ToDoDetail(DetailView):
    model = Homework
    template_name = 'to_do_detail.html'
    success_url = '/to_do/<int:pk>'


class AddAssignment(CreateView):
    form_class = AddAssignment
    model = Assignment
    template_name = 'add_assignment.html'
    success_url = '/to_do'
    def form_valid(self, form):
        name = self.request.user.name
        student = Student.objects.filter(name=name)
        id = self.kwargs['pk']
        homework = get_object_or_404(Homework, pk=id)
        form.instance.student = student.first()
        form.instance.homework = homework
        return super(AddAssignment, self).form_valid(form)
        
        
class Statistics(ListView):
    model = Student
    template_name = 'statistics.html'
    success_url = '/grades'

    def get_context_data(self, *args, **kwargs):
        name = self.request.user.name
        student = get_object_or_404(Student, name=name)
        group = student.group_number
        groupmates = Student.objects.filter(group_number=group)
        context = super(Statistics, self).get_context_data()
        context['groupmates'] = Student.objects.filter(group_number=group)
        context['grades'] = Assessment.objects.filter(student_id__in=groupmates)
        return context
