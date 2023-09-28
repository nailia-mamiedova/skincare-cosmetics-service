from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from cosmetics.models import SkinType

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

    def test_create_member(self):
        skin_type = SkinType.objects.create(
            name="Oily Skin", description="Oily skin type description"
        )
        form_data = {
            "username": "member_test",
            "password1": "test_password_12345",
            "password2": "test_password_12345",
            "first_name": "FirstName",
            "last_name": "LastName",
            "date_of_birth": date(2002, 2, 2),
            "skin_type": skin_type.id,
        }

        response = self.client.post(reverse("cosmetics:member-create"), data=form_data)
        self.assertEqual(response.status_code, 302)

        new_member = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEqual(new_member.first_name, form_data["first_name"])
        self.assertEqual(new_member.last_name, form_data["last_name"])
        self.assertEqual(new_member.date_of_birth, form_data["date_of_birth"])
        self.assertEqual(new_member.skin_type, skin_type)
