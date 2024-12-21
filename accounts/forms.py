from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating new users.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'name']


class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating existing users.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'name', 'is_active', 'new_login']
