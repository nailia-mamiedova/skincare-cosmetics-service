from django.test import TestCase
from django.urls import reverse


BRAND_LIST_URL = reverse("cosmetics:brand-list")


class PublicBrandListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(BRAND_LIST_URL)

        self.assertNotEquals(response.status_code, 200)
