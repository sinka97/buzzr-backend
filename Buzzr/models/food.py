from django.db import models
from .merchant import Merchant

class Food(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    
    AVAILABLE = "ON"
    UNAVAILABLE = "OFF"
    AVAILABILITY_CHOICES = [
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Not Available'),
    ]
    availability = models.CharField(max_length=128, choices=AVAILABILITY_CHOICES, default=UNAVAILABLE)
    
    def __str__(self):
        return f"{self.name} by {self.merchant}"