# Generated by Django 4.2.3 on 2023-07-24 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_mobile_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(blank=True, null=True, verbose_name='موبایل کاربر تایید شده / نشده'),
        ),
    ]
