from django import forms
from .models import Dish
from .models import Order

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['dish', 'customer_name', 'status']
