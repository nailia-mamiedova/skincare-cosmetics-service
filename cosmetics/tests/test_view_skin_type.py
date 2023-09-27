from django.test import TestCase
from django.urls import reverse

SKIN_TYPE_LIST_URL = reverse("cosmetics:skin-type-list")


class PublicSkinTypeListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(SKIN_TYPE_LIST_URL)

        self.assertNotEquals(response.status_code, 200)
