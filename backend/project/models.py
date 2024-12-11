from django.db import models
from django.utils.timezone import now
from client.models import Client 
from masters.models import DocumentType  
from labour_management.models import LaborManagement 


class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    land_facing = models.CharField(max_length=100)
    land_width = models.DecimalField(max_digits=10, decimal_places=2)
    land_breadth = models.DecimalField(max_digits=10, decimal_places=2)
    num_floors = models.IntegerField()
    build_area = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name


class ProjectDocument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, related_name='documents')
    document_name = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True, upload_to='project_documents/')
    uploaded_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.document_name


class LaborToProject(models.Model):
    labor = models.ForeignKey(LaborManagement, on_delete=models.CASCADE, related_name='project_assignments')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='labor_assignments')
    start_date = models.DateField(default=now)
    end_date = models.DateField(blank=True, null=True)

    def get_wages_per_day(self):
        return self.labor.daily_wages

    def calculate_total_earnings(self):
        return sum(transaction.amount for transaction in self.transactions.filter(transaction_type='WORK'))

    def calculate_pending_amount(self):
        total_earnings = self.calculate_total_earnings()
        total_advance = sum(transaction.amount for transaction in self.transactions.filter(transaction_type='ADV'))
        total_payments = sum(transaction.amount for transaction in self.transactions.filter(transaction_type='PAY'))
        return total_earnings - total_advance - total_payments

    def update_earnings(self):
        self.total_earnings = self.calculate_total_earnings()
        self.pending_amount = self.calculate_pending_amount()
        self.save()

    def __str__(self):
        return f"{self.labor.name} assigned to {self.project.project_name}"


class WorkDay(models.Model):
    WORK_TYPES = [
        ('HALF', 'Half-Day'),
        ('FULL', 'Full-Day'),
        ('OT', 'Overtime'),
    ]

    labor_to_project = models.ForeignKey(LaborToProject, on_delete=models.CASCADE, related_name='work_days')
    date = models.DateField()
    work_type = models.CharField(max_length=4, choices=WORK_TYPES, default='FULL')
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2, default=8)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def calculate_hours_worked(self):
        if self.work_type == 'HALF':
            return 4.0
        elif self.work_type == 'FULL':
            return 8.0
        elif self.work_type == 'OT':
            return self.hours_worked + self.overtime_hours
        return 0.0

    def wages(self):
        daily_rate = self.labor_to_project.get_wages_per_day()
        if self.work_type == 'HALF':
            return daily_rate / 2
        elif self.work_type == 'FULL':
            return daily_rate
        elif self.work_type == 'OT':
            regular_pay = daily_rate
            overtime_pay = (daily_rate / 2) * (self.overtime_hours / 8)
            return regular_pay + overtime_pay
        return 0.0

    def save(self, *args, **kwargs):
        self.hours_worked = self.calculate_hours_worked()
        super().save(*args, **kwargs)
        LaborTransaction.objects.update_or_create(
            labor_to_project=self.labor_to_project,
            date=self.date,
            transaction_type='WORK',
            defaults={'amount': self.wages(), 'description': f'{self.get_work_type_display()} work entry'}
        )
        self.labor_to_project.update_earnings()

    def __str__(self):
        return f"{self.date}: {self.get_work_type_display()} ({self.hours_worked} hrs, OT: {self.overtime_hours} hrs)"


class LaborTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('ADV', 'Advance'),
        ('PAY', 'Payment'),
        ('WORK', 'Work Entry'),
    ]

    labor_to_project = models.ForeignKey(LaborToProject, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
    # Automatically adjust advance amounts to be negative
        if self.transaction_type == 'ADV' and self.amount > 0:
            self.amount = -self.amount

        # Ensure payments are positive
        if self.transaction_type == 'PAY' and self.amount < 0:
            raise ValueError("Payment amounts must be positive.")

        super().save(*args, **kwargs)
        self.labor_to_project.update_earnings()

    def __str__(self):
        return f"{self.transaction_type}: {self.amount} on {self.date}"
