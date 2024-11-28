from django import forms
from .models import EmployeeType

class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['name', 'description']
