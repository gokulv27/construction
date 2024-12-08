from django import forms
from .models import EmployeeType, DocumentType, VendorType, LaborSkill

class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['name']


class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ['name']


class LaborSkillForm(forms.ModelForm):
    class Meta:
        model = LaborSkill
        fields = ['name']


class VendorTypeForm(forms.ModelForm):
    class Meta:
        model = VendorType
        fields = ['name']