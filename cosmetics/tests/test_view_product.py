from django.test import TestCase
from django.urls import reverse


PRODUCT_LIST_URL = reverse("cosmetics:product-list")


class PublicProductListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(PRODUCT_LIST_URL)

        self.assertNotEquals(response.status_code, 200)
