from rest_framework import serializers
from .models import CustomUser, OTP
from .util import generate_otp, hash_otp

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'phone_number', 'role', 'status', 'created_at', 'updated_at']

class GenerateOTPSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self, value):
        try:
            self.user = CustomUser.objects.get(username=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        return value

    def save(self, **kwargs):
        raw_otp = generate_otp()
        OTP.objects.create(user=self.user, otp=hash_otp(raw_otp))
        return raw_otp

class ResetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    otp = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = CustomUser.objects.get(username=data['username'])
            otp_instance = OTP.objects.filter(user=user).latest('created_at')
        except (CustomUser.DoesNotExist, OTP.DoesNotExist):
            raise serializers.ValidationError("Invalid username or OTP.")

        if not otp_instance.is_valid() or otp_instance.otp != hash_otp(data['otp']):
            raise serializers.ValidationError("Invalid or expired OTP.")

        self.user = user
        return data

    def save(self, **kwargs):
        self.user.set_password(self.validated_data['new_password'])
        self.user.save()
