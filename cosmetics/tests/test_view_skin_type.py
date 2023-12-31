from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from cosmetics.models import SkinType

SKIN_TYPE_LIST_URL = reverse("cosmetics:skin-type-list")


class PublicSkinTypeListTest(TestCase):
    def test_login_required(self):
        response = self.client.get(SKIN_TYPE_LIST_URL)

        self.assertNotEquals(response.status_code, 200)


class PrivateSkinTypeListTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user",
            password="user12345",
        )
        self.client.force_login(self.user)

    def test_login_required(self):
        res = self.client.get(SKIN_TYPE_LIST_URL)

        self.assertEquals(res.status_code, 200)

    def test_retrieve_skin_type_list(self):
        SkinType.objects.create(
            name="Skin Type", description="Skin Type type description"
        )
        SkinType.objects.create(
            name="Skin Type 2", description="Skin Type description"
        )
        response = self.client.get(SKIN_TYPE_LIST_URL)
        skin_types = SkinType.objects.all()[:4]

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            list(response.context["skin_type_list"]),
            list(skin_types)
        )
        self.assertTemplateUsed(response, "cosmetics/skin_type_list.html")
