from django.urls import path
from . import views

urlpatterns = [
    # Employee Types
    path('employee-types', views.employee_type_list, name='employee_type_list'),
    path('employee-types/create', views.employee_type_create, name='employee_type_create'),
    path('employee-types/update/<int:id>', views.employee_type_update, name='employee_type_update'),
    path('employee-types/delete/<int:id>', views.employee_type_delete, name='employee_type_delete'),

    # Document Types
    path('document-types', views.document_type_list, name='document_type_list'),
    path('document-types/create', views.document_type_create, name='document_type_create'),
    path('document-types/update/<int:id>', views.document_type_update, name='document_type_update'),
    path('document-types/delete/<int:id>', views.document_type_delete, name='document_type_delete'),

    # Vendor Types
    path('vendor-types', views.vendor_type_list, name='vendor_type_list'),                     # GET: List all vendor types
    path('vendor-types/create', views.vendor_type_create, name='vendor_type_create'),          # POST: Create a vendor type
    path('vendor-types/<int:id>/update', views.vendor_type_update, name='vendor_type_update'), # PUT: Update a vendor type
    path('vendor-types/<int:id>/delete', views.vendor_type_delete, name='vendor_type_delete'), # DELETE: Delete a vendor type

    # Labor Skills
    path('skills', views.labor_skill_list, name='labor_skill_list'),                  # GET: List all labor skills
    path('skills/create', views.labor_skill_create, name='labor_skill_create'),          # POST: Create a labor skill
    path('skills/<int:id>/update', views.labor_skill_update, name='labor_skill_update'), # PUT: Update a labor skill
    path('skills/<int:id>/delete', views.labor_skill_delete, name='labor_skill_delete'), # DELETE: Delete a labor skill
]
