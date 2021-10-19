from django.forms import forms
from .models import Student

class StudentForms(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class EditForm(forms.ModelForm):
    id=forms.IntergerField(label='Edit objects with following ID')