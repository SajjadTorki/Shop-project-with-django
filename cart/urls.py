from django.urls import path
from .views import *

app_name = 'cart'
urlpatterns = [
    path('', cart_detail_view, name="cart_detail"),
    path('add_cart/<int:product_id>/', add_to_cart_view, name="cart_add"),
    path('remove_cart/<int:product_id>/', remove_from_cart, name="cart_remove"),

]
