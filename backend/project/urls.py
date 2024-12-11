from django.urls import path
from . import views

urlpatterns = [
    # --- Project CRUD Operations ---
    path('projects/', views.project_list, name='project-list'),
    path('projects/create/', views.project_create, name='project-create'),
    path('projects/<int:id>/update/', views.project_update, name='project-update'),
    path('projects/<int:id>/delete/', views.project_delete, name='project-delete'),

    # --- Project Document Operations ---
    path('projects/documents/upload/', views.UploadDocumentView.as_view(), name='document-upload'),
    path('projects/documents/', views.ProjectDocumentListView.as_view(), name='document-list'),
    path('projects/documents/<int:pk>/', views.ProjectDocumentDetailView.as_view(), name='document-detail'),

    # --- Labor to Project Management ---
    path('projects/<int:project_id>/add-labor/', views.AddLaborToProjectView.as_view(), name='add-labor-to-project'),
    path('projects/<int:project_id>/remove-labor/<int:labor_id>/', views.RemoveLaborFromProjectView.as_view(), name='remove-labor-from-project'),

    # --- WorkDay Management ---
    path('workdays/<int:labor_to_project_id>/', views.WorkDayListView.as_view(), name='workday-list'),
    path('workdays/<int:labor_to_project_id>/create/', views.WorkDayCreateView.as_view(), name='workday-create'),
    path('workdays/<int:workday_id>/update/', views.WorkDayUpdateView.as_view(), name='workday-update'),
    path('workdays/<int:workday_id>/delete/', views.WorkDayDeleteView.as_view(), name='workday-delete'),
]
