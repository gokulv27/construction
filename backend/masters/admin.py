from django.contrib import admin
from .models import EmployeeType

@admin.register(EmployeeType)
class EmployeeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ['name']   # Correct: list
    ordering = ('-created_at',)
