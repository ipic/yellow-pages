from django import forms

from .widgets import GoogleMapsAddressWidget
from .models import Item


class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = ('published', )
        widgets = {
            'address': GoogleMapsAddressWidget,
        }


class AdminAddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'address': GoogleMapsAddressWidget,
        }
