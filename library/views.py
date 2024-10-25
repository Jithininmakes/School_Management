from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse

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
    success_url = reverse_lazy('library:library-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'success': True})


