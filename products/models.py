from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product/product_cover/', verbose_name=_("Product Image"), blank=True, )
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(_('Date Time of Creation'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("product_detail", args=[self.pk])


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    STAR_CHOICES = [
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('normal')),
        ('4', _('good')),
        ('5', _('very good')),
    ]
    author = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(verbose_name=_('Comment Text'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    star = models.CharField(max_length=10, choices=STAR_CHOICES, verbose_name=_('What is your soccer?'))
    active = models.BooleanField(default=True)
    objects = models.Manager
    active_comments_manager = ActiveCommentManager()

    def __str__(self):
        return f'Comment : {self.author}  , product :{self.product}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
