from decimal import Decimal
from django.db import models
from django.utils.timezone import now


class LaborManagement(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone_no = models.CharField(max_length=15, unique=True)
    skill = models.ForeignKey('master.LaborSkill', on_delete=models.CASCADE)
    aadhar_no = models.CharField(max_length=12, unique=True)
    emergency_contact_number = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)
    daily_wages = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # New salary field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WorkDay(models.Model):
    WORK_TYPES = [
        ('HALF', 'Half-Day'),
        ('FULL', 'Full-Day'),
        ('OT', 'Overtime'),
    ]
    labor_to_project = models.ForeignKey(
        'project.LaborToProject',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='work_days'
    )
    adhoc_employee = models.ForeignKey(
        'labour_management.AdHocEmployee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='work_days'
    )
    date = models.DateField()
    work_type = models.CharField(max_length=4, choices=WORK_TYPES, default='FULL')

    def save(self, *args, **kwargs):
        if not self.labor_to_project and not self.adhoc_employee:
            raise ValueError("Either 'labor_to_project' or 'adhoc_employee' must be set.")

        work_amount = self.calculate_work_amount()
        if self.labor_to_project:
            labor = self.labor_to_project.labor
        elif self.adhoc_employee:
            labor = self.adhoc_employee.labor
        else:
            raise ValueError("Invalid labor reference.")

        # Add work amount to the labor's salary
        labor.salary += work_amount
        labor.save()

        super().save(*args, **kwargs)

    def calculate_work_amount(self):
        if self.labor_to_project:
            daily_wages = self.labor_to_project.daily_wages
        elif self.adhoc_employee:
            daily_wages = self.adhoc_employee.labor.daily_wages
        else:
            return 0
        if self.work_type == 'HALF':
            return daily_wages / 2
        elif self.work_type == 'OT':
            return daily_wages * 1.5
        return daily_wages

    def __str__(self):
        assigned_to = self.labor_to_project or self.adhoc_employee
        return f"WorkDay: {assigned_to} on {self.date}"


class LaborTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('ADV', 'Advance'),
        ('PAY', 'Payment'),
    ]

    labor_management = models.ForeignKey(
        'labour_management.LaborManagement',
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES)
    description = models.TextField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['labor_management', 'date', 'transaction_type'],
                name='unique_labor_transaction'
            )
        ]

    def save(self, *args, **kwargs):
        if self.transaction_type == 'PAY':
            self.labor_management.salary -= self.amount
        elif self.transaction_type == 'ADV':
            self.labor_management.salary -= self.amount  # Advance is also deducted from salary
        self.labor_management.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.transaction_type} for {self.labor_management} on {self.date}"

class AdHocEmployee(models.Model):
    labor = models.ForeignKey(
        LaborManagement,
        on_delete=models.CASCADE,
        related_name="adhoc_assignments"
    )
    project = models.ForeignKey(
        'project.Project',  # Reference to the Project model in the project app
        on_delete=models.CASCADE,
        related_name="adhoc_employees"
    )
    hired_date = models.DateField(default=now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"AdHocEmployee: {self.labor.name} assigned to {self.project.project_name}"