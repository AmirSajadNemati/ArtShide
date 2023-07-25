from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _

from contact_us.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message', 'phone']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'نام',
                'required': 'required'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'ایمیل'
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'موضوع'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'پیغام'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'تلفن'
            })

        }

    def __init__(self, *args, **kwargs):
        super(ContactUsModelForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].error_messages = {'required': 'custom required message'}

