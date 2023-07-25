from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'image', 'address', 'about']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'نام'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'نام خانوادگی'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل'
            }),
            'avatar': forms.FileInput(attrs={

            }),
            'address': forms.Textarea(attrs={
               'placeholder': 'آدرس من'
            }),
            'about': forms.Textarea(attrs={
               'placeholder': 'درباره من'
            })
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'avatar': 'تصویر پروفایل',
            'address': 'آدرس',
            'about': 'درباره شخص',
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')
