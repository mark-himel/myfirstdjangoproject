from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from model_utils import Choices

class Merchant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    fax_number = PhoneNumberField(blank=True)
    LOYALTY = Choices((0, 'gold', 'Gold'), (1, 'star', 'Star'), (2, 'platinum', 'Platinum'))
    loyalty = models.IntegerField(choices=LOYALTY, default=LOYALTY.gold)

    def __str__(self):
        return self.name
