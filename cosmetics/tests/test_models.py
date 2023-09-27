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
