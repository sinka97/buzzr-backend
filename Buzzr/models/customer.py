from django.db import models
from .user import User

class Customer(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    user_type = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    total_points = models.BigIntegerField()
    date_joined = models.DateTimeField()
    birthday = models.DateField()
    
    MALE = "M"
    FEMALE = "F"
    UNDEFINED = "NA"
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNDEFINED, 'Undefined'),
    ]
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=UNDEFINED,
        blank=True
    )
    country_code = models.IntegerField(blank=True,null=True)
    phone_number = models.IntegerField()