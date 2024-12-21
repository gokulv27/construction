from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import (
    RegisterSerializer, 
    LoginSerializer, 
    PasswordResetSerializer, 
    UserSerializer
)
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    """
    Handles user registration.
    """
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully."}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Handles user login.
    If the user logs in for the first time (new_login=True),
    they are required to reset the password.
    """
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials."}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_active:
            return Response(
                {"error": "User account is inactive."}, 
                status=status.HTTP_403_FORBIDDEN
            )

        # Check if the user is logging in for the first time
        if user.new_login:
            return Response(
                {
                    "message": "Password reset required.",
                    "user_id": user.id
                }, 
                status=status.HTTP_403_FORBIDDEN
            )

        # Generate JWT tokens for authenticated users
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user_id": user.id
            }, 
            status=status.HTTP_200_OK
        )


class PasswordResetView(APIView):
    """
    Allows unauthenticated users to reset their password
    and returns the user's ID and JWT token upon success.
    """
    permission_classes = [AllowAny]  # Allow access without authentication

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.new_login = False  # Mark as password reset
            user.save()

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "Password reset successfully.",
                    "user_id": user.id,
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(ListAPIView):
    """
    Endpoint to retrieve all users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
