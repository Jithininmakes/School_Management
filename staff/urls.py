from django.urls import path
from .views import StaffListView, StaffCreateView, StaffUpdateView, StaffDeleteView


app_name = 'staff'

urlpatterns = [
    path('list/', StaffListView.as_view(), name='staff_list'),
    path('add/', StaffCreateView.as_view(), name='staff_add'),
    path('edit/<int:pk>/', StaffUpdateView.as_view(), name='staff_edit'),
    path('delete/<int:pk>/', StaffDeleteView.as_view(), name='staff_delete'),
]