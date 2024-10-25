from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import CreateView,FormView
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.views import LogoutView


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'school/register.html'
    success_url = reverse_lazy('login')  # Redirect to login after registration

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = self.request.POST.get('user_type')  # Get user type from the form submission
        user.save()
        login(self.request, user)  # Log in the user after registration
        return redirect('accounts:login')  # Redirect to home or another page after registration



class LoginView(FormView):
    template_name = 'school/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard:admin_dashboard')  # Redirect to home after login

    def form_valid(self, form):
        # Authenticate user and log them in
        user = form.get_user()
        auth_login(self.request, user)

        # Redirect based on user type
        if user.is_admin():
            return redirect('dashboard:admin_dashboard')  # Change to your admin dashboard URL
        elif user.is_staff():
            return redirect('dashboard:officestaff_dashboard')  # Change to your staff dashboard URL
        elif user.is_librarian():
            return redirect('dashboard:librarian_dashboard')  # Change to your librarian dashboard URL
        return redirect(self.success_url)  # Fallback

    def form_invalid(self, form):
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


class LogoutView(LogoutView):
    success_url = reverse_lazy('accounts:login')

    


class IndexView(TemplateView):
    template_name = 'school/index.html'

# Create your views here.


