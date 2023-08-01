from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from course.models import Course


class User(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='تلفن همراه')
    sms_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی پیامکی')
    image = models.ImageField(blank=True, null=True, verbose_name='تصویر کاربر', upload_to='images/users')
    about = models.TextField(blank=True, null=True, verbose_name='درباره ی کاربر')
    address = models.TextField(blank=True, null=True, verbose_name='آدرس')
    is_verified = models.BooleanField(blank=True, null=True, verbose_name='موبایل کاربر تایید شده / نشده')
    course = models.ManyToManyField(to=Course, related_name='user_courses_set',null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username
