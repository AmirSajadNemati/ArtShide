from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account.models import User


class RegisterForm(forms.Form):
    phone = forms.CharField(
        label='شماره همراه',
        max_length=11,
        error_messages={
            'required': 'وارد کردن شماره ی همراه اجباری است.',
            'max_length': 'شماره ی تلفن نمی تواند بیشتر از 11 کاراکتر باشد',
            'min_length': 'شماره ی تلفن نمی تواند کمتر از 11 کاراکتر باشد',
        },
        widget=forms.TextInput(attrs={
            # 'class': 'form-field',
            'placeholder': '*********09'
        }),
        validators=[
            validators.MaxLengthValidator(11, 'شماره ی تلفن نمی تواند بیشتر از 11 کاراکتر باشد'),
            validators.MinLengthValidator(11, 'شماره ی تلفن نمی تواند کمتر از 11 کاراکتر باشد')
        ],

    )

    username = forms.CharField(
        label='نام کاربری',
        max_length=50,
        error_messages={
            'required': 'لطفا نام کاربری خود را وارد کنید',
            'max_length': 'نام کاربری نمی تواند بیشتر از 50 کاراکتر باشد'
        },
        widget=forms.TextInput(attrs={

            'placeholder': 'نام کاربری'
        })
    )

    password = forms.CharField(
        label='کلمه ی عبور',
        error_messages={
            'required': 'پر کردن این فیلد اجباری است.',
        },
        widget=forms.PasswordInput(attrs={
            'id': 'reg_password',

            'placeholder': 'کلمه ی عبور'
        })
    )

    confirm_password = forms.CharField(
        label='تکرار کلمه ی عبور',
        error_messages={
            'required': 'پر کردن این فیلد اجباری است.',
        },
        widget=forms.PasswordInput(attrs={
            'id': 'reg_password2',
            'placeholder': 'تکرار کلمه ی عبور'
        })
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        user_exists_by_phone = User.objects.filter(phone=phone).exists()
        if user_exists_by_phone:
            raise forms.ValidationError("شماره همراه وارد شده قبلا ثبت نام شده است !")
        return phone

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        raise ValidationError("کلمه ی عبور و تکرار آن با هم مغایرت دارند!")


class LoginForm(forms.Form):
    phone = forms.CharField(
        label='شماره همراه',
        max_length=11,
        error_messages={
            'required': 'لطفا شماره همراه خود را وارد کنید',
            'max_length': ''
        },
        widget=forms.TextInput(attrs={
            # 'class': 'form-field',
            'placeholder': '09********'
        })
    )

    password = forms.CharField(
        label='کلمه ی عبور',
        widget=forms.PasswordInput(attrs={
            # 'class': 'form-field',

        })
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )

class SMSActiveCodeForm(forms.Form):
    activation_code = forms.CharField(
        error_messages={
            'required': 'لطفا کد ارسال شده را وارد کنید',
            'max_length': ''
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'کد ارسال شده به تلفن همراه شما'
        })
    )