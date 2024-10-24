from django import forms
from .models import Librarian

class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['first_name', 'last_name', 'email', 'phone_number']