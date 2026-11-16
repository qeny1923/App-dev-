from django import forms
from .models import StudentDetails, Book

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['name', 'email', 'age']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year_published']

