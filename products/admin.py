from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product, Comment


# Register your models here.

class CommentsInline(admin.TabularInline):
    model = Comment
    filter = ['product', 'active', 'datetime_created', 'star']


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['title', 'price', 'active', 'datetime_created']
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'active', 'datetime_created', 'star']
