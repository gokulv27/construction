from django.urls import path
from . import views

urlpatterns = [
    # Employee Types
    path('api/employee-types/', views.employee_type_list, name='employee_type_list'),
    path('api/employee-types/create/', views.employee_type_create, name='employee_type_create'),
    path('api/employee-types/update/<int:id>/', views.employee_type_update, name='employee_type_update'),
    path('api/employee-types/delete/<int:id>/', views.employee_type_delete, name='employee_type_delete'),

    # Document Types
    path('api/document-types/', views.document_type_list, name='document_type_list'),
    path('api/document-types/create/', views.document_type_create, name='document_type_create'),
    path('api/document-types/update/<int:id>/', views.document_type_update, name='document_type_update'),
    path('api/document-types/delete/<int:id>/', views.document_type_delete, name='document_type_delete'),

    # Vendor Types
    path('api/vendor-types/', views.vendor_type_list, name='vendor_type_list'),                     # GET: List all vendor types
    path('api/vendor-types/create/', views.vendor_type_create, name='vendor_type_create'),          # POST: Create a vendor type
    path('api/vendor-types/<int:id>/update/', views.vendor_type_update, name='vendor_type_update'), # PUT: Update a vendor type
    path('api/vendor-types/<int:id>/delete/', views.vendor_type_delete, name='vendor_type_delete'), # DELETE: Delete a vendor type

    # Labor Skills
    path('api/skills/', views.labor_skill_list, name='labor_skill_list'),                  # GET: List all labor skills
    path('api/skills/create/', views.labor_skill_create, name='labor_skill_create'),          # POST: Create a labor skill
    path('api/skills/<int:id>/update/', views.labor_skill_update, name='labor_skill_update'), # PUT: Update a labor skill
    path('api/skills/<int:id>/delete/', views.labor_skill_delete, name='labor_skill_delete'), # DELETE: Delete a labor skill
]
