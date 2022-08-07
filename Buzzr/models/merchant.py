from django.db import models
from .user import User
from multiselectfield import MultiSelectField
from ..utils import get_current_datetime

# TODO:
# (1) Add options like ratings and halal certificates etc. using MultiSelectField
#      reference: https://pypi.org/project/django-multiselectfield/

class Merchant(models.Model):
    id = models.BigAutoField(primary_key=True)
    uen = models.CharField(max_length=10)                                                               # Filled by Merchant
    name = models.CharField(max_length=255)                                                             # Filled by Merchant (Shop name)
    country_code = models.IntegerField(blank=True,null=True)                                            # Filled by Merchant
    phone_number = models.CharField(max_length=255, blank=True, null=True)                              # Filled by Merchant
    
    # TODO (1):
    
    unit = models.CharField(max_length=5, blank=True)                                                   # Filled by Merchant
    block = models.CharField(max_length=5, blank=True)                                                  # Filled by Merchant
    street = models.CharField(max_length=128, blank=True)                                               # Filled by Merchant
    address = models.CharField(max_length=255)                                                          
    postal_code = models.IntegerField()                                                                 # Filled by Merchant
    district = models.IntegerField()
    date_joined = models.DateField(auto_now_add=True)
    
    MERCHANT_TYPE_CHOICES = [
        ('HAW', 'Hawker'),
        ('HOT', 'Restaurant'),
        ('RES', 'Hotel'),
        ('UND', 'UNDEFINED'),
    ]
    type = models.CharField(max_length=3,choices=MERCHANT_TYPE_CHOICES, default='UND')                  # Filled by Merchant
    
    CUISINE_CHOICES = [
        ('CHI', 'Chinese'),
        ('IND', 'Indian'),
        ('MALAY', 'Malay'),
        ('WEST', 'Western'),
        ('VEG', 'Vegetarian'),
        ('DRINKS', 'DRINKS'),
        ('FUSION','FUSION'),
        ('NIL', 'UNDEFINED'),
    ]
    cuisine = MultiSelectField(choices=CUISINE_CHOICES,
                                 max_choices=3,
                                 max_length=6)                                                          # Filled by Merchant    
    
    OPERATION_STATUS_CHOICES = [
        ('OPEN', 'Open for Business'),
        ('TEMP', 'Temporarily Closed'),
        ('PH', 'Closed for Public Holiday'),
        ('PERM', 'Permanently Closed'),
    ]
    operation_status = models.CharField(max_length=255, default="TEMP")
    
    # TODO (1): ADD RATINGS AND CERTIFICATES (e.g. HALAL) 
    ##############################################################################
    ##############################################################################

    def __str__(self):
        return "Merchant: " + str(self.name) + " located at " + str(self.address)
    
    # def save(self, *args, **kwargs):
    #     self.address = f'#{self.unit} BLK {self.block} {self.street}, {self.postal_code}'
        

class MerchantSchedule(models.Model):
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    DAY_OF_WEEK_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES)
    
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    
    