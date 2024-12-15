from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .serializers import UserSerializer, GenerateOTPSerializer, ResetPasswordSerializer
from .util import send_telegram_message
from .models import CustomUser

class UserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = CustomUser(
                username=serializer.validated_data['username'],
                name=serializer.validated_data.get('name', ''),
                phone_number=serializer.validated_data['phone_number'],
                role=serializer.validated_data['role'],
                status=serializer.validated_data['status']
            )

            # Reject passwords that look hashed
            if data['password'].startswith("$2b$"):
                return Response({"error": "Hashed passwords are not allowed."}, status=400)

            user.set_password(data['password'])  # Hash password securely
            user.save()
            return Response({"message": "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)

        # Reject passwords or usernames that look like hashed strings (e.g., bcrypt hash patterns)
        if isinstance(password, str) and password.startswith("$2b$"):
            raise AuthenticationFailed("Invalid credentials. Hashed password not allowed as input.")
        
        if isinstance(username, str) and username.startswith("$2b$"):
            raise AuthenticationFailed("Invalid credentials. Hashed username not allowed as input.")

        # Use Django's authenticate method to verify credentials
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed("Invalid credentials")

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class SendOTPView(APIView):
    def post(self, request):
        serializer = GenerateOTPSerializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.save()
            user = serializer.user

            if not user.telegram_chat_id:
                return Response({"error": "User has not linked their Telegram account."}, status=status.HTTP_400_BAD_REQUEST)

            telegram_response = send_telegram_message(user.telegram_chat_id, f"Your OTP is: {otp}")
            if telegram_response and telegram_response.get("ok"):
                return Response({"message": "OTP sent successfully via Telegram."})
            else:
                return Response({"error": "Failed to send OTP via Telegram."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def handle_telegram_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", {})
        chat = message.get("chat", {})
        text = message.get("text", "")
        chat_id = chat.get("id")

        if text.startswith('/start'):
            send_telegram_message(chat_id, "Hi! Please reply with your phone number to link your account.")
            return JsonResponse({"status": "awaiting_phone_number"})

        if text.startswith('+91'):
            phone_number = text.strip()
            try:
                user = CustomUser.objects.get(phone_number=phone_number)
                user.telegram_chat_id = chat_id
                user.save()
                send_telegram_message(chat_id, "Your account has been linked! You will receive OTPs here.")
                return JsonResponse({"status": "linked"})
            except CustomUser.DoesNotExist:
                send_telegram_message(chat_id, "Phone number not found in our system.")
                return JsonResponse({"status": "error", "message": "Phone number not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password reset successful."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    # permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access this view

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)