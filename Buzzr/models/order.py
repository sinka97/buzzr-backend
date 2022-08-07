from random import choices
from django.db import models
from .merchant import Merchant
from .food import Food
from .customer import Customer


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING,null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.DO_NOTHING)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank=True,null=True)
    points = models.IntegerField(null=True)
    
    WAIT = "Waiting"
    IN_QUEUE = "Queuing"
    PREP = "Preparing"
    READY = "Ready"
    STATUS_CHOICES = [
        (WAIT, f'Waiting for confirmation from {merchant}.'),
        (IN_QUEUE, 'Order placed.'),
        (PREP, 'Restaurant is preparing.'),
        (READY, 'Ready for collection.'),
    ]
    status = models.CharField(max_length=50,choices=STATUS_CHOICES)
