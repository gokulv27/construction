from django.urls import path
from . import views

urlpatterns = [
    path('', views.labor_list, name='labor_list'),
    path('create/', views.labor_create, name='labor_create'),
    path('update/', views.labor_update, name='labor_update'),
    path('<int:id>/delete/', views.labor_delete, name='labor_delete'),
]
