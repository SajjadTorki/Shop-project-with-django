from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('comment/<int:pk>/', CommentView.as_view(), name="comment_created"),
]
