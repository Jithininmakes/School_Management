from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('librarian', 'Librarian'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, null=True)

    def is_admin(self):
        return self.user_type == 'admin'

    def is_staff(self):
        return self.user_type == 'staff'

    def is_librarian(self):
        return self.user_type == 'librarian'
