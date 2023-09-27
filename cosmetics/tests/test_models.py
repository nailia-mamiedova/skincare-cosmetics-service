from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase
from cosmetics.models import Brand, SkinType, Product


class ModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.brand = Brand.objects.create(
            name="BrandName",
            country="CountryName"
        )
        cls.skin_type = SkinType.objects.create(
            name="Oily", description="Oily skin type description"
        )
        cls.product = Product.objects.create(
            name="ProductName",
            brand=cls.brand,
            ingredients="Water, Sugar",
            description="A test product",
        )
        cls.member = get_user_model().objects.create(
            username="testuser",
            first_name="FirstName",
            last_name="LastName",
            date_of_birth=date(2000, 1, 1),
            skin_type=cls.skin_type,
        )

    def test_brand_str(self):
        self.assertEqual(str(self.brand), "BrandName (CountryName)")

    def test_skin_type_str(self):
        self.assertEqual(str(self.skin_type), "Oily")

    def test_product_str(self):
        self.assertEqual(str(self.product), "BrandName ProductName")

    def test_member_str(self):
        self.assertEqual(str(self.member), "testuser (FirstName LastName)")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.member.get_absolute_url(),
            f"/members/{self.member.pk}/detail/"
        )
