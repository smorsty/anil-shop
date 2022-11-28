from django import forms


from shop.models import OrderItem


class AddQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']


# form for size field here
#blank=True, null=True)

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
