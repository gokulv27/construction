from django.urls import path
from . import views

urlpatterns = [
    # Project CRUD operations
    path('api/projects/', views.project_list, name='project_list'),
    path('api/projects/create/', views.project_create, name='project_create'),
    path('api/projects/update/<int:id>/', views.project_update, name='project_update'),
    path('api/projects/delete/<int:id>/', views.project_delete, name='project_delete'),

    # Project document handling
    path('api/projects/documents/upload/', views.UploadDocumentView.as_view(), name='upload_document'),
    path('api/projects/documents/', views.ProjectDocumentListView.as_view(), name='project_document_list'),
    path('api/projects/documents/<int:pk>/', views.ProjectDocumentDetailView.as_view(), name='project_document_detail'),
]
