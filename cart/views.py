from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import AddToCartProductForm


# Create your views here.


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True
        })
    return render(request,
                  "cart/cart_detail.html",
                  {
                      'cart': cart,
                  })


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        clean_data = form.cleaned_data
        quantity = clean_data['quantity']
        cart.add(product, quantity, replace_current_quantity=clean_data['inplace'])

    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
