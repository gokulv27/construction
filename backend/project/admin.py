from django.contrib import admin
from .models import Project, ProjectDocument

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client', 'location', 'budget', 'active_status', 'created_at', 'updated_at')
    list_filter = ('active_status', 'location')
    search_fields = ('project_name', 'client__name', 'location')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(ProjectDocument)
class ProjectDocumentAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'project', 'uploaded_at')
    search_fields = ('document_name', 'project__project_name')
    readonly_fields = ('uploaded_at',)
