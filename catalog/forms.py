from django import forms
from django.conf import settings
from django.core.mail import send_mail

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

    class Media:
        js = ('js/mw_google_point_field.js', )
        css = {
            'all': ('css/custom.css', )
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=255)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)
    captcha = CaptchaField()

    def save(self):
        cleaned = self.cleaned_data
        subject = '[BUSQIPIC] Nova mensagem de contato'
        message = """
Mensagem:
    {}
""".format(cleaned['message'])
        try:
            send_mail(subject, message, cleaned['email'],
                      [settings.DEFAULT_FROM_EMAIL, 'ellisonleao@gmail.com'])
        except:
            pass
