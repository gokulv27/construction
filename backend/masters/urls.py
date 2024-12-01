from django.urls import path
from . import views

urlpatterns = [
    path('api/employee-types/', views.employee_type_list, name='employee_type_list'),
    path('api/employee-types/create/', views.employee_type_create, name='employee_type_create'),
    path('api/employee-types/update/<int:id>/', views.employee_type_update, name='employee_type_update'),
    path('api/employee-types/delete/<int:id>/', views.employee_type_delete, name='employee_type_delete'),
]
    
    #  path('vendor_types/', views.vendor_type_list, name='vendor_type_list'),
    # path('vendor_types/create/', views.vendor_type_create, name='vendor_type_create'),
    # path('vendor_types/update/<int:id>/', views.vendor_type_update, name='vendor_type_update'),
    # path('vendor_types/delete/<int:id>/', views.vendor_type_delete, name='vendor_type_delete'),
   

    # path('brand-type/', views.brand_type_list, name='brand_type_list'),
    # path('brand-type/create/', views.brand_type_create, name='brand_type_create'),
    # path('brand-type/update/<int:id>/', views.brand_type_update, name='brand_type_update'),
    # path('brand-type/delete/<int:id>/', views.brand_type_delete, name='brand_type_delete'),

    # path('employee-rolles/', views.employee_rolles_list, name='employee_rolles_list'),
    # path('employee-rolles/create/', views.employee_rolles_create, name='employee_rolles_create'),
    # path('employee-rolles/update/<int:id>/', views.employee_rolles_update, name='employee_rolles_update'),
    # path('employee-rolles/delete/<int:id>/', views.employee_rolles_delete, name='employee_rolles_delete'),
    
    # path('item/', views.item_list, name='item_list'),  # List all items
    # path('item/create/', views.item_create, name='item_create'),  # Create a new item
    # path('item/update/<int:id>/', views.item_update, name='item_update'),  # Update an existing item
    # path('item/delete/<int:id>/', views.item_delete, name='item_delete'),  # Delete an item
    


