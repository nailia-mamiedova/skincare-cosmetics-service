from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from cosmetics.models import Brand, Product

PRODUCT_LIST_URL = reverse("cosmetics:product-list")


class PublicProductListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(PRODUCT_LIST_URL)

        self.assertNotEquals(response.status_code, 200)


class PrivateProductListTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user", password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_product_list(self):
        brand = Brand.objects.create(name="BrandName", country="Japan")
        Product.objects.create(
            name="Product1",
            brand=brand,
            ingredients="Ingredients1, Ingredients2",
            description="Description",
        )
        Product.objects.create(
            name="Product2",
            brand=brand,
            ingredients="Ingredients1, Ingredients2",
            description="Description",
        )
        response = self.client.get(PRODUCT_LIST_URL)
        products = Product.objects.all()[:4]

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            list(response.context["product_list"]),
            list(products)
        )
        self.assertTemplateUsed(response, "cosmetics/product_list.html")
