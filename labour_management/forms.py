from django import forms
from .models import LaborManagement

class LaborManagementForm(forms.ModelForm):
    class Meta:
        model = LaborManagement
        fields = [
            'name', 'phone_no', 'skill', 'aadhar_no', 'emergency_contact_number',
            'address', 'city', 'state', 'pincode', 'daily_wages'
        ]
