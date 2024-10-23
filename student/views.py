from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm



class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student:student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student:student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_delete.html'
    success_url = reverse_lazy('student:student-list')
