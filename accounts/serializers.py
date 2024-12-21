from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'phone_number', 'name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is inactive.")
        if user.new_login:
            raise serializers.ValidationError(
                "Password reset required before proceeding."
            )
        return {
            "user_id": user.id,
            "username": user.username,
        }


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for password reset.
    """
    username = serializers.CharField(max_length=150)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = CustomUser.objects.get(username=data['username'])
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        return data

    def save(self):
        validated_data = self.validated_data
        user = CustomUser.objects.get(username=validated_data['username'])
        user.set_password(validated_data['new_password'])
        user.new_login = False  # Mark password reset complete
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve user information.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'phone_number', 'name', 'created_at', 'updated_at']
