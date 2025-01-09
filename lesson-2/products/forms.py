from django import forms
from products.models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price", "stock_count")

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Price cannot be negative")
        return price

    def clean_stock_count(self):
        stock_count = self.cleaned_data.get("stock_count")
        if stock_count < 0:
            raise ValidationError("Stock cannot be negative")
        return stock_count
