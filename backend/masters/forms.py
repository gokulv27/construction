# masters/forms.py
from django import forms
from .models import EmployeeType

class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['name']

# class vendortypeForm(forms.ModelForm):
#     class Meta:
#         model = vendortype
#         fields = ['name']

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