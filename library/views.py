from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from .models import Library
from .forms import LibraryForm



class LibraryListView(ListView):
    model = Library
    template_name = 'library/library_list.html'


class LibraryList1View(ListView):
    model = Library
    template_name = 'library/library_list1.html'



class LibraryCreateView(CreateView):
    model = Library
    form_class = LibraryForm
    template_name = 'library/library_form.html'
    success_url = reverse_lazy('library:library-list')

class LibraryUpdateView(UpdateView):
    model = Library
    form_class = LibraryForm
    template_name = 'library/library_form.html'
    success_url = reverse_lazy('library:library-list')

class LibraryDeleteView(DeleteView):
    model = Library
    template_name = 'library/library_delete.html'
    success_url = reverse_lazy('library:library-list')


