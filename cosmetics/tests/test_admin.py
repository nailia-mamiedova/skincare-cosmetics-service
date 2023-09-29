from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from cosmetics.models import SkinType, Product, Brand


class AdminSiteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin_user = get_user_model().objects.create_superuser(
            username="test_user",
            password="test_password_12345"
        )
        cls.skin_type = SkinType.objects.create(name="Skin Type")
        cls.brand = Brand.objects.create(name="The Ordinary")
        cls.product = Product.objects.create(
            name="Niacinamide 10% + Zinc 1%",
            brand=cls.brand,
        )

    def setUp(self) -> None:
        self.client.force_login(self.admin_user)
        self.member = get_user_model().objects.create_user(
            username="member",
            password="member12345",
            date_of_birth=date(2002, 2, 2),
        )
        self.member.favorite_products.add(self.product)
        self.member.skin_type = self.skin_type
        self.member.save()

    def test_member_skin_type_listed(self):
        url = reverse("admin:cosmetics_member_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.skin_type)

    def test_member_skin_type_detailed(self):
        url = reverse("admin:cosmetics_member_change", args=[self.member.id])
        response = self.client.get(url)

        self.assertContains(response, self.skin_type)

    def test_member_favorite_products_detailed(self):
        url = reverse("admin:cosmetics_member_change", args=[self.member.id])
        response = self.client.get(url)

        self.assertContains(response, self.product)

    def test_member_date_of_birth_listed(self):
        url = reverse("admin:cosmetics_member_changelist")
        response = self.client.get(url)

        self.assertContains(
            response, self.member.date_of_birth.strftime("%b. %d, %Y").replace(" 0", " ")
        )

    def test_member_detailed_date_of_birth_listed(self):
        url = reverse("admin:cosmetics_member_change", args=[self.member.id])
        response = self.client.get(url)

        self.assertContains(response, self.member.date_of_birth)
