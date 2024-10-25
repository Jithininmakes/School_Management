from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,StudentList1View

app_name = 'student'


urlpatterns = [
    path('list/', StudentListView.as_view(), name='student-list'),
    path('list1/', StudentList1View.as_view(), name='student-list1'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
]
