from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False, verbose_name=_('Paid'))
    first_name = models.CharField(verbose_name=_('FirstName'), max_length=100)
    last_name = models.CharField(verbose_name=_('LastName'), max_length=100)
    order_notes = models.CharField(_('Order Notes'), max_length=700, blank=True)
    phone_number = models.CharField(verbose_name=_('phone number'), max_length=12)
    address = models.CharField(verbose_name=_('Address'), max_length=700)
    datetime_created = models.DateTimeField(_('Created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Modified'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('Order'))
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items',
                                verbose_name=_('Product'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Quantity'))
    price = models.PositiveIntegerField(verbose_name=_('Price'))

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} x {self.quantity} (price:{self.price})'
