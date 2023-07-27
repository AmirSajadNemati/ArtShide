from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='تلفن همراه')
    sms_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی پیامکی')
    image = models.ImageField(blank=True, null=True, verbose_name='تصویر کاربر', upload_to='images/users')
    about = models.TextField(blank=True, null=True, verbose_name='درباره ی کاربر')
    address = models.TextField(blank=True, null=True, verbose_name='آدرس')
    is_verified = models.BooleanField(blank=True, null=True, verbose_name='موبایل کاربر تایید شده / نشده')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username
