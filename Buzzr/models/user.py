from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    
    CUSTOMER = 'CU'
    EMPLOYEE = "MM"
    GROUP_MANAGER = "GM"
    SUPER_USER = "SU"
    ROLE_CHOICES = [
        (CUSTOMER, "Customer"),
        (EMPLOYEE, 'Merchant Manager'),
        (GROUP_MANAGER, 'Group Manager'),
        (SUPER_USER, 'Super User'),
    ]
    
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=128,unique=True)
    display_name = models.CharField(max_length=255)
    role = models.CharField(
        max_length = 5,
        choices=ROLE_CHOICES,
        default="CU"
    )
    state = models.JSONField(null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    def __str__(self):
        return "User: " + self.display_name + ", Role: " + self.role
    
    