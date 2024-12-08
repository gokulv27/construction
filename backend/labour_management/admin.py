from django.contrib import admin
from .models import  LaborManagement




@admin.register(LaborManagement)
class LaborManagementAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'phone_no', 'aadhar_no', 'city', 'state', 'pincode', 
        'daily_wages', 'created_at', 'updated_at'
    )  # Removed 'document_type'
    list_filter = ('city', 'state')  # Removed 'document_type'
    search_fields = ('name', 'phone_no', 'aadhar_no', 'city', 'state')
    ordering = ('-created_at',)
    fieldsets = (
        ("Basic Information", {
            'fields': ('name', 'phone_no', 'aadhar_no', 'emergency_contact_number')
        }),
        ("Address", {
            'fields': ('address', 'city', 'state', 'pincode')
        }),
        ("Job Details", {
            'fields': ('daily_wages',)
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at')
        }),
    )  # Removed 'document_type' here
    readonly_fields = ('created_at', 'updated_at')

