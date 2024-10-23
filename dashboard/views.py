from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Role-based mixins
from .mixins import AdminRequiredMixin, OfficeStaffRequiredMixin, LibrarianRequiredMixin


@method_decorator(login_required, name='dispatch')
class AdminView(AdminRequiredMixin, TemplateView):
    template_name = 'dashboard/admin_dashboard.html'



@method_decorator(login_required, name='dispatch')
class OfficeStaffView(OfficeStaffRequiredMixin, TemplateView):
    template_name = 'dashboard/officestaff_dashboard.html'



@method_decorator(login_required, name='dispatch')
class LibrarianView(LibrarianRequiredMixin, TemplateView):
    template_name = 'dashboard/librarian_dashboard.html'

