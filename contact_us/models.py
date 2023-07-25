from django.db import models

# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان', db_index=True)
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن تماس با ما')
    response = models.TextField(verbose_name='متن پاسخ تماس با ما')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    is_read = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return f'{self.title} by {self.full_name}'
