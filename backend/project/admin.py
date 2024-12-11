from django.contrib import admin
from .models import Project, ProjectDocument, LaborToProject, LaborManagement, WorkDay, LaborTransaction


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client', 'location', 'budget', 'active_status', 'created_at', 'updated_at')
    list_filter = ('active_status', 'location')
    search_fields = ('project_name', 'client__name', 'location')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('client',)


@admin.register(ProjectDocument)
class ProjectDocumentAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'project', 'uploaded_at')
    search_fields = ('document_name', 'project__project_name')
    readonly_fields = ('uploaded_at',)


@admin.register(LaborToProject)
class LaborToProjectAdmin(admin.ModelAdmin):
    list_display = ('labor', 'project', 'start_date', 'end_date', 'get_wages_per_day')
    list_filter = ('project', 'start_date', 'end_date')
    search_fields = ('labor__name', 'project__project_name')
    autocomplete_fields = ('labor', 'project')

    def get_wages_per_day(self, obj):
        return obj.get_wages_per_day()
    get_wages_per_day.short_description = "Daily Wages (Labor)"


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'labor_to_project', 'work_type', 'hours_worked', 'overtime_hours', 'calculate_wages')
    list_filter = ('work_type', 'date', 'labor_to_project__project')
    search_fields = ('labor_to_project__labor__name', 'labor_to_project__project__project_name')
    autocomplete_fields = ('labor_to_project',)

    def calculate_wages(self, obj):
        return obj.wages()
    calculate_wages.short_description = "Calculated Wages"


@admin.register(LaborTransaction)
class LaborTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'amount', 'labor_to_project', 'date', 'description')
    list_filter = ('transaction_type', 'date')
    search_fields = ('labor_to_project__labor__name', 'labor_to_project__project__project_name')
    autocomplete_fields = ('labor_to_project',)
