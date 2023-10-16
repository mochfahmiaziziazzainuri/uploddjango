from django import forms
from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'custumer' : forms.Select(attrs={'class': 'form-control'}),
             'product' : forms.Select(attrs={'class': 'form-control'}),
              'status' : forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'custumer': 'konsumen',
            'product': 'produk',
            'status': 'status order',
        }

