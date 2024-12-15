from django import forms
from .models import DocumentType, VendorType, LaborSkill ,UserRole



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

class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['name']