from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib import messages


# Role-based mixins


@method_decorator(login_required, name='dispatch')
class AdminView( TemplateView):
    template_name = 'dashboard/admin_dashboard.html'

    def get(self, request, *args, **kwargs):
        messages.success(request, "Welcome to the Admin Dashboard!")
        return super().get(request, *args, **kwargs)



@method_decorator(login_required, name='dispatch')
class OfficeStaffView( TemplateView):
    template_name = 'dashboard/officestaff_dashboard.html'

    def get(self, request, *args, **kwargs):
        messages.success(request, "Welcome to the Staff Dashboard!")
        return super().get(request, *args, **kwargs)




@method_decorator(login_required, name='dispatch')
class LibrarianView( TemplateView):
    template_name = 'dashboard/librarian_dashboard.html'

    def get(self, request, *args, **kwargs):
        messages.success(request, "Welcome to the Librarian Dashboard!")
        return super().get(request, *args, **kwargs)


