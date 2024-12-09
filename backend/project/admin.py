from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client', 'location', 'budget', 'active_status', 'created_at', 'updated_at')
    list_filter = ('active_status', 'location')
    search_fields = ('project_name', 'client__name', 'location')
    readonly_fields = ('created_at', 'updated_at')
