from django import forms

from cars.models import Car
from .models import Order


class OrderForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=Car.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ["car", "name", "phone"]
