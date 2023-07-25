from django.contrib import admin

from . import models

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_read']
    list_editable = ['is_read']


admin.site.register(models.ContactUs, ContactUsAdmin)
