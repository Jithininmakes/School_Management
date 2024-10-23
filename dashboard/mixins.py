from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

# Mixin for Admin
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_admin  # Assuming is_admin is a Boolean field in your User model

    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to access this page.")

# Mixin for Office Staff
class OfficeStaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_office_staff  # Assuming is_office_staff is a Boolean field

    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to access this page.")

# Mixin for Librarian
class LibrarianRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_librarian  # Assuming is_librarian is a Boolean field

    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to access this page.")
