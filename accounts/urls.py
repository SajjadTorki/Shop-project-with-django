from django.urls import path

from . import views

urlpatterns = [
    path('signin/', views.SignInPageView.as_view(), name='signin')

]
