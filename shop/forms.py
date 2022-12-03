from django import forms
from shop.models import OrderItem


class AddQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']


class PickSizeForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['size']

class ProductPriceFilterFrom(forms.Form):
    min_price = forms.IntegerField(label="min", required=False)
    max_price = forms.IntegerField(label="max", required=False)
    ordering = forms.ChoiceField(label="sort", required=False, choices=[
        ["name", "alphabet"],
        ["price", "cheap first"],
        ["-price", "expensive first"],
    ])


class CheckoutForm(forms.Form):
    first_name = forms.CharField(label='first_name', required=True)
    last_name = forms.CharField(label='last_name', required=True)
    country = forms.CharField(label='country', required=True)
    city = forms.CharField(label='city', required=True)
    street = forms.CharField(label='street', required=True)
    home_number = forms.CharField(label='home_number', required=True)
    zip = forms.CharField(label='zip', required=True)
    phone = forms.CharField(label='phone', required=True)
    comment = forms.CharField(label='comment', required=False)
    # telegram_username = forms.CharField(label='telegram_username', widget=forms.Textarea, required=True)
    # blank=True, null=True)
