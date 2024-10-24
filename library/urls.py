
from django.urls import path
from .views import LibraryListView, LibraryCreateView,LibraryUpdateView,LibraryDeleteView


app_name= 'library'

urlpatterns = [
    path('librarylist/', LibraryListView.as_view(), name='library-list'),
    path('librarycreate/', LibraryCreateView.as_view(), name='library-create'),
    path('update/<int:pk>/', LibraryUpdateView.as_view(), name='library-update'),
    path('delete/<int:pk>/', LibraryDeleteView.as_view(), name='library-delete'),
]


