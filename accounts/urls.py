from django.urls import path
from .views import RegisterView, LoginView, PasswordResetView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('users/', UserListView.as_view(), name='user_list'),
]
