from django.shortcuts import render, reverse
from django.views import generic
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartProductForm


# Create your views here.


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()

        return context


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=product_id)
        obj.product = product
        messages.success(self.request, _("Comment success create!"))
        return super().form_valid(form)
