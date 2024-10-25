
from django.urls import path
from .views import LibraryListView, LibraryCreateView,LibraryUpdateView,LibraryDeleteView,LibraryList1View


app_name= 'library'

urlpatterns = [
    path('librarylist/', LibraryListView.as_view(), name='library-list'),
    path('librarylist1/', LibraryList1View.as_view(), name='library-list1'),
    path('librarycreate/', LibraryCreateView.as_view(), name='library-create'),
    path('update/<int:pk>/', LibraryUpdateView.as_view(), name='library-update'),
    path('delete/<int:pk>/', LibraryDeleteView.as_view(), name='library-delete'),
]


