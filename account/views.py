from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from account.forms import RegisterForm, SMSActiveCodeForm, LoginForm
from account.models import User
from utils.sms_kaveh import send_activation_code_sms
from utils.random_number_by_digits_generator import random_number_by_digits_generator
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST, use_required_attribute=False)

        if register_form.is_valid():
            user_phone = register_form.cleaned_data.get('phone')
            user_password = register_form.cleaned_data.get('password')
            username = register_form.cleaned_data.get('username')
            new_user = User(
                phone=user_phone,
                sms_active_code=random_number_by_digits_generator(7),
                is_verified=False,
                username=username
            )
            new_user.set_password(user_password)
            new_user.save()

            # todo: send activation code
            return redirect(reverse('login-page'))
        else:
            context = {
                'register_form': register_form
            }
            print(register_form.errors)
            return render(request, 'account/register_page.html', context)


# @method_decorator(login_required, name='dispatch')

class ActivateAccountView(View):
    def get(self, request):
        sms_active_code_form = SMSActiveCodeForm()
        context = {
            'sms_active_code_form': sms_active_code_form
        }

        return render(request, 'account/sms_active_code.html', context)

    def post(self, request):
        sms_active_code_form = SMSActiveCodeForm(request.POST)
        if sms_active_code_form.is_valid():
            user_active_code = request.user.sms_active_code
            active_code = sms_active_code_form.cleaned_data.get('activation_code')
            user: User = User.objects.filter(sms_active_code__iexact=user_active_code).first()
            if user is not None:
                if active_code == user.sms_active_code:
                    user.is_verified = True
                    user.save()
                    return redirect(reverse('home-page'))
                else:
                    sms_active_code_form.add_error('activation_code', 'کد وارد شده اشتباه می باشد')
            else:
                sms_active_code_form.add_error('activation_code', 'کاربری یافت نشد')


        context = {
            'sms_active_code_form': sms_active_code_form
        }
        return render(request, 'account/sms_active_code.html', context)


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'account/login_page.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_phone = login_form.cleaned_data.get('phone')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(phone__iexact=user_phone).first()
            if user is not None:
                is_password_correct = user.check_password(user_pass)
                if is_password_correct:
                    login(request, user)
                    if not user.is_verified:
                        send_activation_code_sms(user.phone, f'کد فعالسازی شماره همراه شما {user.sms_active_code}')
                        return redirect(reverse('activate-account-page'))
                    else:
                        return redirect(reverse('home-page'))
                else:
                    login_form.add_error('password', 'کاربری با مشخصات وارد شده یافت نشد')
            else:
                login_form.add_error('password', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }
        return render(request, 'account/login_page.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-page'))
