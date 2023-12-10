from django.test import TestCase
from django.shortcuts import reverse

from .models import Product


# Create your tests here.


class ProductTest(TestCase):
    def setUp(self):
        self.product_obj = Product.objects.create(
            id=1,
            title="book",
            description='best',
            price=2000,
            active=True,

        )

    def test_product_list_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.client.get(f'/products/{self.product_obj.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_details_page(self):
        response = self.client.get(reverse('product_detail', args=[self.product_obj.id]))
        self.assertContains(response, self.product_obj.title)
