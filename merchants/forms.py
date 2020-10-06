from django import forms
from phonenumber_field.formfields import PhoneNumberField
from merchants.models import Merchant

class NewForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    email_address = forms.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    fax_number = PhoneNumberField()

    class Meta:
        model = Merchant
        fields = ('name', 'location', 'email_address', 'phone_number', 'fax_number',)
