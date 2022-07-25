from dataclasses import field

from django import forms
from item.models import ProductModel

class AddItem(forms.Modelform):
    class Meta:
        model=ProductModel
        field = '__all__'