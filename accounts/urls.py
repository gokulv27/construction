from django.urls import path
from .views import RegisterView, LoginView,  UserListView,SendOTPView,ResetPasswordView,UserListView,handle_telegram_webhook

urlpatterns = [
    path('user/', UserListView.as_view(), name='user_list'), 
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('roles/', UserListView.as_view(), name='roles'),
    path('telegram-webhook/', handle_telegram_webhook, name='telegram-webhook'),
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]
