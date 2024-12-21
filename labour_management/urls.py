from django.urls import path
from . import views

urlpatterns = [
    path('', views.labor_list, name='labor_list'),
    path('create/', views.labor_create, name='labor_create'),
    path('<int:id>/update/', views.labor_update, name='labor_update'),
    path('<int:id>/delete/', views.labor_delete, name='labor_delete'),
       # AdHocEmployee URLs
    path('adhoc-employees/', views.adhoc_employee_list, name='adhoc-employee-list'),
    path('adhoc-employees/create/', views.adhoc_employee_create, name='adhoc-employee-create'),
    path('adhoc-employees/<int:id>/update/', views.adhoc_employee_update, name='adhoc-employee-update'),
    path('adhoc-employees/<int:id>/delete/', views.adhoc_employee_delete, name='adhoc-employee-delete'),

    # WorkDay URLs
    path('workdays/', views.workday_list, name='workday-list'),
    path('workdays/create/', views.workday_create, name='workday-create'),
    path('workdays/<int:id>/update/', views.workday_update, name='workday-update'),
    path('workdays/<int:id>/delete/', views.workday_delete, name='workday-delete'),

    # LaborTransaction URLs
    path('labor-transactions/', views.labor_transaction_list, name='labor-transaction-list'),
    path('labor-transactions/create/', views.labor_transaction_create, name='labor-transaction-create'),
    path('labor-transactions/<int:id>/update/', views.labor_transaction_update, name='labor-transaction-update'),
    path('labor-transactions/<int:id>/delete/', views.labor_transaction_delete, name='labor-transaction-delete'),
]
