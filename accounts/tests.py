from django.test import TestCase
from django.shortcuts import reverse
from .models import CustomUser


# Create your tests here.


class TestAccount(TestCase):

    def test_login_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_template_name(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
