from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    customer_tags = models.TextField(help_text="Comma-separated tags", blank=True, null=True)
    country = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    name = models.CharField(max_length=201, unique=True, editable=False)  # Auto-generated unique field

    def save(self, *args, **kwargs):
        # Combine first_name and last_name to create a unique name
        self.name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_name_constraint')
        ]

    def __str__(self):
        return self.name
