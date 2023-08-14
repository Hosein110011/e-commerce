from django.db import models
from billing.models import BillingProfile


ADDRESS_TYPES = (
    ('billing','Billing'),
    ('shipping','Shipping'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=125, choices=ADDRESS_TYPES)
    address_line_1 = models.CharField(max_length=125)
    address_line_2 = models.CharField(max_length=125, blank=True, null=True)
    city = models.CharField(max_length=125)
    country = models.CharField(max_length=125, default='United State of America')
    state = models.CharField(max_length=125)
    postal_code = models.CharField(max_length=125)

    def __str__(self):
        return str(self.billing_profile)
    
    
    
