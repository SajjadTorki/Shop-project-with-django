from django.test import TestCase
from django.shortcuts import reverse


# Create your tests here.


class PageTest(TestCase):
    def test_pages_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_pages_template_name(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "<h1>Home Page</h1>")
        self.assertEqual(response.status_code, 200)
