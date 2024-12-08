from django.urls import path
from . import views

urlpatterns = [
    path('api/labors/', views.labor_list, name='labor-list'),
    path('api/labors/create/', views.labor_create, name='labor-create'),
    path('api/labors/<int:id>/update/', views.labor_update, name='labor-update'),
    path('api/labors/<int:id>/delete/', views.labor_delete, name='labor-delete'),
    path('api/csrf/', views.get_csrf_token, name='csrf-token'),
     
]
