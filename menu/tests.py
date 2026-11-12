from decimal import Decimal

from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Category, MenuItem
from .templatetags.menu_extras import currency


class MenuItemModelTests(TestCase):
    def test_str_returns_name(self):
        item = MenuItem(name="Tomato soup", price=Decimal("5.50"))
        self.assertEqual(str(item), "Tomato soup")

    def test_new_item_is_available_by_default(self):
        item = MenuItem.objects.create(name="Bread", price=Decimal("2.00"))
        self.assertTrue(item.is_available)


class MenuViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Runs once for this class. Each test gets a fresh, empty test database.
        soups = Category.objects.create(name="Soups")
        cls.soup = MenuItem.objects.create(
            name="Tomato soup", price=Decimal("5.50"), category=soups
        )
        cls.hidden = MenuItem.objects.create(
            name="Secret dish", price=Decimal("99.00"), is_available=False
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("menu:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/home.html")

    def test_home_shows_only_available_items(self):
        response = self.client.get(reverse("menu:home"))
        self.assertContains(response, "Tomato soup")
        self.assertNotContains(response, "Secret dish")

    def test_item_detail_shows_item(self):
        url = reverse("menu:item_detail", args=[self.soup.pk])
        response = self.client.get(url)
        self.assertContains(response, "Tomato soup")
        self.assertContains(response, "$5.50")
        self.assertContains(response, "Soups")

    def test_hidden_item_returns_404(self):
        url = reverse("menu:item_detail", args=[self.hidden.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_missing_item_returns_404(self):
        response = self.client.get(reverse("menu:item_detail", args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_hello_escapes_html(self):
        response = self.client.get(reverse("menu:hello", args=["<script>"]))
        self.assertContains(response, "&lt;script&gt;")
        self.assertNotContains(response, "<script>")

    def test_home_uses_a_single_database_query(self):
        # select_related("category") fetches items AND their categories in 1 query.
        with self.assertNumQueries(1):
            self.client.get(reverse("menu:home"))

    def test_timing_middleware_adds_header(self):
        response = self.client.get(reverse("menu:home"))
        self.assertIn("X-Response-Time-ms", response)


class CurrencyFilterTests(SimpleTestCase):
    def test_adds_dollar_sign_and_two_decimals(self):
        self.assertEqual(currency(Decimal("5.5")), "$5.50")

    def test_adds_thousands_separator(self):
        self.assertEqual(currency(1234), "$1,234.00")
