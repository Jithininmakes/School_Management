from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,DeleteView,UpdateView
from .models import Fee
from .forms import FeeForm

class FeeListView(ListView):
    model = Fee
    template_name = 'fees/fee_list.html'

class FeeCreateView(CreateView):
    model = Fee
    form_class = FeeForm
    template_name = 'fees/fee_form.html'
    success_url = reverse_lazy('fees:fee-list')


class FeeUpdateView(UpdateView):
    model = Fee
    form_class = FeeForm
    template_name = 'fees/fee_form.html' 
    success_url = reverse_lazy('fees:fee-list')

class FeeDeleteView(DeleteView):
    model = Fee
    template_name = 'fees/fee_delete.html'
    success_url = reverse_lazy('fees:fee-list')