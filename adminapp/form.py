from django import forms
from adminapp.models import MessageModel

class MessageForm(forms.ModelForm):
    class Meta:
        model=MessageModel
        fields ="__all__"