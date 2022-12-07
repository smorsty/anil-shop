from django import forms
from shop.models import OrderItem, Product

PRODUCT_TYPE_CHOICE = (
    ('Одежда',
     (
        ('t-shirt', 'Футболки'),
        ('shirt', 'Рубашки'),
        ('polo', 'Поло'),
        ('sweater', 'Свитера'),
        ('hoodie', 'Худи'),
        ('turtleneck', 'Водолазки'),
        ('Longs-Leeve', 'Лонгсливы'),

        ('shorts', 'Шорты'),
        ('trousers', 'Брюки'),
        ('jeans', 'Джинсы'),
        ('sport_trousers', 'Спортивные штаны'),

        ('bomber', 'Бомберы'),
        ('jacket', 'Куртки'),
        ('vest', 'Жилетки'),
        ('coat', 'Пальто'),
        ('park', 'Парки'),
        ('down jacket', 'Пуховики'),

        ('sport_costumes', 'Спортивные костюмы'),
     )
    ),
    ('Обувь',
     (
        ('sneakers', 'Кроссовки'),
        ('boots', 'Ботинки'),
        ('flip_flops', 'Тапки'),
        ('sandals', 'Сандали'),

     )
     ),
    ('Аксессуары',
     (
        ('accessories', 'Аксессуары'),
     )
     ),
    ('Техника',
     (
         ('dyson', 'DYSON'),

     )
    ),
)

class AddQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']


class PickSizeForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['size']

class PickTypeForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['product_type']

class ProductPriceFilterFrom(forms.Form):
    min_price = forms.IntegerField(label="от", required=False)
    max_price = forms.IntegerField(label="до", required=False)
    ordering = forms.ChoiceField(label="сортировка", required=False, choices=[
        ["name", "по умолчанию"],
        ["price", "сначала дешевые"],
        ["-price", "сначала дорогие"],
    ])


class ProductTypeFilterForm(forms.Form):
    category = forms.ChoiceField(label="категория", required=False, choices=PRODUCT_TYPE_CHOICE)

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


