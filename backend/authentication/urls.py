from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),           # GET: List users
    path('users/create/', views.UserCreateView.as_view(), name='user-create'), # POST: Create a user
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'), # GET: Retrieve a single user
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'), # PUT/PATCH: Update a user
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'), # DELETE: Delete a user
]
