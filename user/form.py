from django import forms
from user.models import UserCartModel

class CartForm():
    class Meta:
        model=UserCartModel
        fields ="__all__"