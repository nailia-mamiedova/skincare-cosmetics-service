from datetime import date
from django.test import TestCase
from cosmetics.forms import MemberCreationForm, MemberUpdateForm
from cosmetics.models import SkinType


class MemberFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.skin_type = SkinType.objects.create(name="Skin Type")

    def test_member_creation_form_is_valid(self):
        form_data = {
            "username": "test_user",
            "password1": "test_password_12345",
            "password2": "test_password_12345",
            "first_name": "Test First",
            "last_name": "Test Last",
            "date_of_birth": date(2002, 2, 2),
            "skin_type": self.skin_type.id,
        }
        form = MemberCreationForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_member_update_form_is_valid(self):
        form_data = {
            "username": "test_user",
            "first_name": "Test First",
            "last_name": "Test Last",
            "date_of_birth": date(2002, 2, 2),
            "skin_type": self.skin_type.id,
        }

        form = MemberUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
