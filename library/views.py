from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Library
from .forms import LibraryForm



class LibraryListView(ListView):
    model = Library
    template_name = 'library/library_list.html'



class LibraryCreateView(CreateView):
    model = Library
    form_class = LibraryForm
    template_name = 'library/library_form.html'
    success_url = reverse_lazy('library:library-list')

