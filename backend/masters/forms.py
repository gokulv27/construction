# masters/forms.py
from django import forms
from .models import EmployeeType,DocumentType,VendorType

class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['name']

class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ['name']


class VendortypeForm(forms.ModelForm):
    class Meta:
        model = VendorType
        fields = ['name']

# class BrandTypeForm(forms.ModelForm):
#     class Meta:
#         model = BrandType
#         fields = ['name']

        
# class EmployeeRollesForm(forms.ModelForm):
#     class Meta:
#         model = EmployeeRolles
#         fields = ['name']

# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ['name', 'brand']  # Include only the fields that should be editable
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
#             'brand': forms.Select(attrs={'class': 'form-control'}),
#         }