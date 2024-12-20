from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLES = [('Admin', 'Admin'), ('Supervisor', 'Supervisor'), ('Client', 'Client')]
    STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)  # Changed to CharField for names
    role = models.CharField(max_length=50, choices=ROLES, default='Client')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Active')
    created_by = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Add unique related_name attributes to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Custom related_name
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.username