from django.urls import path
from . import views

urlpatterns = [
    path('api/employeetypes/', views.employee_type_list, name='employee_type_list'),
    path('api/employeetypes/create/', views.employee_type_create, name='employee_type_create'),
    path('api/employeetypes/<int:id>/update/', views.employee_type_update, name='employee_type_update'),
    path('api/employeetypes/<int:id>/delete/', views.employee_type_delete, name='employee_type_delete'),
]
