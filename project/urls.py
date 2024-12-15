from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Project routes
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:id>/update/', views.project_update, name='project_update'),
    path('projects/<int:id>/delete/', views.project_delete, name='project_delete'),

    # Project Document routes
    path('projects/<int:project_id>/documents/', views.project_document_list, name='project_document_list_by_project'),
    path('documents/', views.project_document_list, name='project_document_list'),
    path('documents/create/', views.project_document_create, name='project_document_create'),
    path('documents/<int:id>/update/', views.project_document_update, name='project_document_update'),
    path('documents/<int:id>/delete/', views.project_document_delete, name='project_document_delete'),
    path('documents/<int:id>/download/', views.project_document_download, name='project_document_download'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)