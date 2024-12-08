from django.urls import path
from . import views

urlpatterns = [
    path('api/labors/', views.labor_list, name='labor_list'),
    path('api/labors/create/', views.labor_create, name='labor_create'),
    path('api/labors/<int:id>/update/', views.labor_update, name='labor_update'),
    path('api/labors/<int:id>/delete/', views.labor_delete, name='labor_delete'),
]
