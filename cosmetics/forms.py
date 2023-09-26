from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError


def validate_date_of_birth(date_of_birth):
    if date_of_birth.year < datetime.now().year - 99:
        raise ValidationError("You cannot be that old")
    elif date_of_birth.year > datetime.now().year:
        raise ValidationError("You are not born yet")
    elif date_of_birth.year > datetime.now().year - 18:
        raise ValidationError("You should be at least 18 years old")

    return date_of_birth


class BrandSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class ProductSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class SkinTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class MemberSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )
