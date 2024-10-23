from django.urls import path
from .views import AdminView, OfficeStaffView, LibrarianView

app_name = 'dashboard'

urlpatterns = [
    path('admin', AdminView.as_view(), name='admin_dashboard'),
    path('office_staff', OfficeStaffView.as_view(), name='officestaff_dashboard'),
    path('librarian', LibrarianView.as_view(), name='librarian_dashboard'),
]
