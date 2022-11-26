from django import forms

from shop.models import OrderItem


class AddQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']

# form for size field here

class CheckoutForm(forms.Form):
    country = forms.CharField(label='country', widget=forms.Textarea, required=True)
    first_name = forms.CharField(label='first_name', widget=forms.Textarea, required=True)
    last_name = forms.CharField(label='last_name', widget=forms.Textarea, required=True)
    street = forms.CharField(label='street', widget=forms.Textarea, required=True)
    home_number = forms.CharField(label='home_number', widget=forms.Textarea, required=True)
    city = forms.CharField(label='city', widget=forms.Textarea, required=True)
    zip = forms.CharField(label='zip', widget=forms.Textarea, required=True)
    phone = forms.CharField(label='phone', widget=forms.Textarea, required=True)
    # telegram_username = forms.CharField(label='telegram_username', widget=forms.Textarea, required=True)
