from django.db import models
from .order import Order
from .food import Food


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    total_price = models.FloatField()
    
class CartItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity = models.IntegerField()