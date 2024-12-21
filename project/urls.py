from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Project routes
    path('', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('<int:id>/update/', views.project_update, name='project_update'),
    path('<int:id>/delete/', views.project_delete, name='project_delete'),

    # Document routes
    path('document/<int:project_id>/list/', views.project_document_list, name='project_document_list_by_project'),
    path('document/', views.project_document_list, name='project_document_list'),
    path('document/create/', views.project_document_create, name='project_document_create'),
    path('document/<int:id>/update/', views.project_document_update, name='project_document_update'),
    path('document/<int:id>/delete/', views.project_document_delete, name='project_document_delete'),
    path('document/<int:id>/download/', views.project_document_download, name='project_document_download'),

    # LaborToProject routes
    path('labor-to-project/', views.labor_to_project_list, name='labor_to_project_list'),
    path('labor-to-project/create/', views.labor_to_project_create, name='labor_to_project_create'),
    path('labor-to-project/<int:id>/update/', views.labor_to_project_update, name='labor_to_project_update'),
    path('labor-to-project/<int:id>/delete/', views.labor_to_project_delete, name='labor_to_project_delete'),

 

   
]