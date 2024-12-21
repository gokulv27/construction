from decimal import Decimal
from django.db import models
from django.utils.timezone import now


class Project(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    land_facing = models.CharField(max_length=100)
    land_width = models.DecimalField(max_digits=10, decimal_places=2)
    land_breadth = models.DecimalField(max_digits=10, decimal_places=2)
    num_floors = models.IntegerField()
    build_area = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name


class Document(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='documents')
    document_type = models.ForeignKey('master.DocumentType', on_delete=models.CASCADE, related_name='documents')
    document_name = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True, upload_to='project_documents/')
    uploaded_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.document_name


class LaborToProject(models.Model):
    labor = models.ForeignKey('labour_management.LaborManagement', on_delete=models.CASCADE, related_name='project_assignments')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='labor_assignments')
    start_date = models.DateField(default=now)
    end_date = models.DateField(blank=True, null=True)
    daily_wages = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    ad_hoc_employee = models.ForeignKey('labour_management.AdHocEmployee', on_delete=models.SET_NULL, null=True, blank=True, related_name='labor_to_projects')

    def calculate_daily_wages(self, date):
        """
        Calculates daily wages for a specific labor, project, and date.
        Ensures no duplicate records exist for the same labor, project, and date.
        """
        from labour_management.models import WorkDay  # Lazy import to avoid circular dependency

        if WorkDay.objects.filter(labor_to_project=self, date=date).exists():
            raise ValueError(f"A work entry already exists for labor {self.labor.id}, project {self.project.id}, and date {date}.")

        return self.daily_wages

    def __str__(self):
        return f"{self.labor} - {self.project}"
