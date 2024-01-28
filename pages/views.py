from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


def about_us_view(request):
    return render(request, 'about_us.html')
