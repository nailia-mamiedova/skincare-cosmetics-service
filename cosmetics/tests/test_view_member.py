from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

MEMBER_LIST_URL = reverse("cosmetics:member-list")


class PublicMemberListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(MEMBER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateMemberListTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user", password="user12345"
        )
        self.client.force_login(self.user)
