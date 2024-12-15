from django.urls import path
from . import views

urlpatterns = [

    # Document Types
    path('document-type/', views.document_type_list, name='document_type_list'),
    path('document-type/create/', views.document_type_create, name='document_type_create'),
    path('document-type/update/<int:id>/', views.document_type_update, name='document_type_update'),
    path('document-type/delete/<int:id>/', views.document_type_delete, name='document_type_delete'),

    # Vendor Types
    path('vendor-type/', views.vendor_type_list, name='vendor_type_list'),                     # GET: List all vendor types
    path('vendor-type/create/', views.vendor_type_create, name='vendor_type_create'),          # POST: Create a vendor type
    path('vendor-type/<int:id>/update/', views.vendor_type_update, name='vendor_type_update'), # PUT: Update a vendor type
    path('vendor-type/<int:id>/delete/', views.vendor_type_delete, name='vendor_type_delete'), # DELETE: Delete a vendor type

    # Labor Skills
    path('skill/', views.labor_skill_list, name='labor_skill_list'),                  # GET: List all labor skills
    path('skill/create/', views.labor_skill_create, name='labor_skill_create'),          # POST: Create a labor skill
    path('skill/<int:id>/update/', views.labor_skill_update, name='labor_skill_update'), # PUT: Update a labor skill
    path('skill/<int:id>/delete/', views.labor_skill_delete, name='labor_skill_delete'), # DELETE: Delete a labor skill

    path('user_roles/', views.user_role_list, name='user_role_list'),
    path('user_roles/create/', views.user_role_create, name='user_role_create'),
    path('user_roles/update/<int:id>/', views.user_role_update, name='user_role_update'),
    path('user_roles/delete/<int:id>/', views.user_role_delete, name='user_role_delete'),
]
