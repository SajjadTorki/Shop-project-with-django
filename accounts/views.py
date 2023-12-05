from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import *


# Create your views here.


class SignInPageView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')
