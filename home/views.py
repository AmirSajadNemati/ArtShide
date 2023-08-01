from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from site_settings.models import SiteSliderSection, SliderImages, SiteSetting


class HomeView(View):
    def get(self, request: HttpResponse):
        slider_images = SliderImages.objects.filter(slider_section__section='home')
        context = {
            'slider_images': slider_images,
            'settings': SiteSetting.objects.all().first()

        }

        return render(request, 'home/index.html', context)


class AboutUsView(TemplateView):
    template_name = 'about_us/about_us.html'


def site_header_component(request):
    context = {
        'settings': SiteSetting.objects.all().first()
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    context = {
        'settings': SiteSetting.objects.all().first()
    }
    return render(request, 'shared/site_footer_component.html', context)


def handler_404_error(request, exception):
    return render(request, '404.html', {})
