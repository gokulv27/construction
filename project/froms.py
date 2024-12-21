from django import forms
from .models import LaborToProject,Project, Document

# Project Form
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'client', 'project_name', 'location', 'budget', 'land_facing', 
            'land_width', 'land_breadth', 'num_floors', 'build_area', 'active_status'
        ]
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Document Form
class ProjectDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['project', 'document_name', 'file']
        widgets = {
            'document_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# LaborToProject Form
class LaborToProjectForm(forms.ModelForm):
    class Meta:
        model = LaborToProject
        fields = ['labor', 'project', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

