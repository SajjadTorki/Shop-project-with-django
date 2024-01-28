from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about_Us/', views.about_us_view, name='about_us'),

]
