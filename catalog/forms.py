from django import forms

from .widgets import GoogleMapsAddressWidget
from .models import Item

from captcha.fields import CaptchaField
from mapwidgets.widgets import GooglePointFieldWidget


class AddItemForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Item
        exclude = ('published', 'user')
        widgets = {
            'location': GooglePointFieldWidget,
            'categories': forms.SelectMultiple(attrs={'class': 'ui dropdown'}),
            'address': forms.TextInput(attrs={'id': 'address-mw-google-address-input'})
        }


class AdminAddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'location': GooglePointFieldWidget,
            'address': forms.TextInput(attrs={'id': 'address-mw-google-address-input'})
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=255)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem', widget=forms.TextInput)
    captcha = CaptchaField()

    def save(self):
        cleaned = self.cleaned_data()
        return
