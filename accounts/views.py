from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import RegisterForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'school/register.html'
    success_url = reverse_lazy('home')  # Redirect to login after registration

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log in the user after registration
        return redirect('home')  # Redirect to home or another page after registration


# Create your views here.
class HomeView(TemplateView):
    template_name = 'school/home.html'

