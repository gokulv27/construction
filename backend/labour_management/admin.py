from django.contrib import admin
from .models import LaborManagement

@admin.register(LaborManagement)
class LaborManagementAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'phone_no', 'aadhar_no', 'city', 'state', 'pincode', 
        'daily_wages', 'skill', 'created_at', 'updated_at'
    )
    list_filter = ('city', 'state', 'skill')
    search_fields = ('name', 'phone_no', 'aadhar_no', 'city', 'state', 'skill__name')
    ordering = ('-created_at',)
    fieldsets = (
        ("Basic Information", {
            'fields': ('name', 'phone_no', 'aadhar_no', 'emergency_contact_number', 'skill')
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
    )
    readonly_fields = ('created_at', 'updated_at')
