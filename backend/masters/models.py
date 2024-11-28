from django.db import models

class EmployeeType(models.Model):
    # Define available employee types as choices
    EMPLOYEE_TYPE_CHOICES = [
        ('Admin', 'Admin'),
        ('Site Supervisor', 'Site Supervisor'),
        ('Engineer', 'Engineer'),
        ('Manager', 'Manager'),
        ('Technician', 'Technician'),
    ]

    name = models.CharField(
        max_length=255,
        choices=EMPLOYEE_TYPE_CHOICES,  # Restrict to defined choices
        unique=True  # Ensure each type is only listed once
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Employee Type"
        verbose_name_plural = "Employee Types"

    def __str__(self):
        return f"{self.name}"

