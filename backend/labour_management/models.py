from django.db import models




class LaborManagement(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone_no = models.CharField(max_length=15, unique=True)
    aadhar_no = models.CharField(max_length=12, unique=True)
    emergency_contact_number = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)
    daily_wages = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
