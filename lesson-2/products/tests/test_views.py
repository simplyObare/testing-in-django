from django.test import TestCase, SimpleTestCase
from products.models import Product
from django.urls import reverse


class TestHomePage(SimpleTestCase):

    def test_homepage_uses_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")

    def test_homepage_contains_welcome_message(self):
        response = self.client.get("/")
        self.assertContains(response, "Welcome to our store", status_code=200)


class TestProductsPage(TestCase):
    def setUp(self):
        Product.objects.create(name="Laptop", price=1000.00, stock_count=10)
        Product.objects.create(name="Phone", price=800.00, stock_count=25)

    def test_products_page_uses_correct_template(self):
        response = self.client.get(reverse("products"))
        self.assertTemplateUsed(response, "products.html")

    def test_products_context(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(len(response.context["products"]), 2)
        self.assertContains(response, "Laptop")
        self.assertContains(response, "Phone")
        self.assertNotContains(response, "No products found")

    def test_products_view_when_there_is_no_product(self):
        Product.objects.all().delete()
        response = self.client.get(reverse("products"))
        self.assertContains(response, "No products found")
        self.assertEqual(len(response.context["products"]), 0)
