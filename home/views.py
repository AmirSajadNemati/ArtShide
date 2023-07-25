from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'

class AboutUsView(TemplateView):
    template_name = 'about_us/about_us.html'

def site_header_component(request):
    context = {
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    context = {

    }
    return render(request, 'shared/site_footer_component.html', context)
