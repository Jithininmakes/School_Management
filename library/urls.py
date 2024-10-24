
from django.urls import path
from .views import LibraryListView, LibraryCreateView


app_name= 'library'

urlpatterns = [
    path('librarylist/', LibraryListView.as_view(), name='library-list'),
    path('librarycreate/', LibraryCreateView.as_view(), name='library-create'),
]


