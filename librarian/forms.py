from django import forms
from .models import Librarian

class StaffForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['first_name', 'last_name', 'email', 'phone_number']