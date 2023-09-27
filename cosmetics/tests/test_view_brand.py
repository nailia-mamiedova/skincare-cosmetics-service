from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from cosmetics.models import Brand

BRAND_LIST_URL = reverse("cosmetics:brand-list")


class PublicBrandListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(BRAND_LIST_URL)

        self.assertNotEquals(response.status_code, 200)


class PrivateBrandListTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user",
            password="user12345",
        )
        self.client.force_login(self.user)

    def test_login_required(self):
        res = self.client.get(BRAND_LIST_URL)

        self.assertEquals(res.status_code, 200)
