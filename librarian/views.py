from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from .models import Librarian
from .forms import LibrarianForm

class LibrarianListView(ListView):
    model = Librarian
    template_name = 'librarian/librarian_list.html'
    context_object_name = 'librarian_list'


class LibrarianCreateView(CreateView):
    model = Librarian
    form_class = LibrarianForm
    template_name = 'librarian/librarian_form.html'
    success_url = reverse_lazy('librarian:librarian_list')

    def form_valid(self, form):
        return super().form_valid(form)


class LibrarianUpdateView(UpdateView):
    model = Librarian
    form_class = LibrarianForm
    template_name = 'librarian/librarian_form.html'
    success_url = reverse_lazy('librarian:librarian_list')


class LibrarianDeleteView(DeleteView):
    model = Librarian
    template_name = 'librarian/librarian_delete.html'
    success_url = reverse_lazy('librarian:librarian_list')

