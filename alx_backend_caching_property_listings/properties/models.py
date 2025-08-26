import uuid
from django.db import models
from django.core.exceptions import ValidationError

class Property(models.Model):
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        if self.price <= 0:
            raise ValidationError("Price must be greater than zero.")
        
    def __str__(self):
        return self.title