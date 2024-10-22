from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import RegisterForm,LoginForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'school/register.html'
    success_url = reverse_lazy('login')  # Redirect to login after registration

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log in the user after registration
        return redirect('login')  # Redirect to home or another page after registration



class LoginView(FormView):
    template_name = 'school/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')  # Redirect to home after login

    def form_valid(self, form):
        login(self.request, form.get_user())  # Log in the user
        return super().form_valid(form)


# Create your views here.
class HomeView(TemplateView):
    template_name = 'school/home.html'

