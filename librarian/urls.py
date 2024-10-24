from django.urls import path
from .views import LibrarianCreateView, LibrarianListView, LibrarianUpdateView, LibrarianDeleteView


app_name = 'librarian'

urlpatterns = [
     path('list/', LibrarianListView.as_view(), name='librarian_list'),
    path('add/', LibrarianCreateView.as_view(), name='librarian_add'),
    path('edit/<int:pk>/', LibrarianUpdateView.as_view(), name='librarian_edit'),
    path('delete/<int:pk>/', LibrarianDeleteView.as_view(), name='librarian_delete'),
]