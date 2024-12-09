from django.urls import path
from .views import (
    project_list, project_create, project_update, project_delete
)

urlpatterns = [
    # Project URLs
    path('projects/', project_list, name='project_list'),
    path('projects/create/', project_create, name='project_create'),
    path('projects/update/<int:id>/', project_update, name='project_update'),
    path('projects/delete/<int:id>/', project_delete, name='project_delete'),
]
