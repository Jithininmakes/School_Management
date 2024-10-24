from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from .models import Staff
from .forms import StaffForm

class StaffListView(ListView):
    model = Staff
    template_name = 'staff/staff_list.html'
    context_object_name = 'staff_list'


class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff/staff_form.html'
    success_url = reverse_lazy('staff:staff_list')

    def form_valid(self, form):
        return super().form_valid(form)


class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff/staff_form.html'
    success_url = reverse_lazy('staff:staff_list')


class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'staff/staff_confirm_delete.html'
    success_url = reverse_lazy('staff:staff_list')

