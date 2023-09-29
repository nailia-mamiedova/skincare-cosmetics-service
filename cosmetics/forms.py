from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from cosmetics.models import Member


def validate_date_of_birth(date_of_birth):
    if date_of_birth.year < datetime.now().year - 99:
        raise ValidationError("You cannot be that old")
    elif date_of_birth.year > datetime.now().year:
        raise ValidationError("You are not born yet")
    elif date_of_birth.year > datetime.now().year - 18:
        raise ValidationError("You should be at least 18 years old")

    return date_of_birth


class MemberCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        required=False,
        validators=[validate_date_of_birth],
        help_text="Enter the date in the format: YYYY-MM-DD.",
    )

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = UserCreationForm.Meta.fields + (
            "date_of_birth",
            "skin_type",
            "first_name",
            "last_name",
        )

    def clean_date_of_birth(self):
        return validate_date_of_birth(self.cleaned_data["date_of_birth"])


class MemberUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        help_text="Enter the date in the format: YYYY-MM-DD."
    )

    class Meta:
        model = Member
        fields = (
            "username",
            "first_name",
            "last_name",
            "date_of_birth",
            "skin_type",
        )

    def clean_date_of_birth(self):
        return validate_date_of_birth(self.cleaned_data["date_of_birth"])


class BrandSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class ProductSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class SkinTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class MemberSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )
