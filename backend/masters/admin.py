# masters/admin.py
from django.contrib import admin
from .models import EmployeeType,DocumentType,VendorType

admin.site.register(EmployeeType)
admin.site.register(DocumentType)
admin.site.register(VendorType)
admin.site.register(BrandType)
# admin.site.register(EmployeeRolles)
# admin.site.register(Item)