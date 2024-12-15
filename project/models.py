from django.db import models
from master.models import DocumentType
from client.models import Client
from django.utils.timezone import now

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, related_name='documents')
    document_name = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True, upload_to='project_documents/')
    uploaded_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.document_name

