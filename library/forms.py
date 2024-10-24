from django import forms
from .models import Library

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['student', 'book_title', 'issue_date', 'return_date']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'book_title': forms.TextInput(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
        }
