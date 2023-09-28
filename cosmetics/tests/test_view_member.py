from django.test import TestCase
from django.urls import reverse

MEMBER_LIST_URL = reverse("cosmetics:member-list")


class PublicMemberListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(MEMBER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)
