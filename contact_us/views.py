from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from contact_us.forms import ContactUsModelForm


class ContactUsView(FormView):
    template_name = 'contact_us/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        # context['site_setting'] = setting

        return context

    def form_valid(self, form):

        form.save()
        return super(ContactUsView, self).form_valid(form)
