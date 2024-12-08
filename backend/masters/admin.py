from django.contrib import admin
from .models import EmployeeType, DocumentType, VendorType, LaborSkill

# Register models for the Django admin interface
admin.site.register(EmployeeType)
admin.site.register(DocumentType)
admin.site.register(VendorType)
admin.site.register(LaborSkill)
