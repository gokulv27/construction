from datetime import timedelta
from hashlib import sha256
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+91\d{10}$',
                message="Phone number must be entered in the format: '+91XXXXXXXXXX'. Exactly 10 digits allowed after +91."
            )
        ]
    )
    role = models.ForeignKey('master.UserRole', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
        default='Active'
    )
    telegram_chat_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk is None and hasattr(self, 'password'):
            self.set_password(self.password)  # Ensure password is hashed on creation
        super().save(*args, **kwargs)

class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return now() < self.created_at + timedelta(minutes=5)

    def save(self, *args, **kwargs):
        if not self.pk:  # Hash OTP only on creation
            self.otp = sha256(self.otp.encode()).hexdigest()
        super().save(*args, **kwargs)
