from django.db import models
from django.contrib.auth.models import User
from apps.store.models import Country

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shipping_addresses')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    street_address_1 = models.TextField()
    street_address_2 = models.TextField(null=True, blank=True)
    closest_landmark = models.CharField(max_length=255 ,null=True, blank=True, help_text='The closest large building or known place to the customers house')
    city_area = models.CharField(max_length=255, null=True, blank=True) # Add the help text
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=40, null=True, blank=True)
    state_division = models.CharField(max_length=255)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=80)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'