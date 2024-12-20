from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'customer_tags',
            'country', 'address', 'city', 'postal_code'
        ]
