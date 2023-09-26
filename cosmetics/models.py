from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class SkinType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "skin type"
        verbose_name_plural = "skin types"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    skin_types = models.ManyToManyField(SkinType, related_name="products")
    ingredients = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.brand.name} {self.name}"


class Member(AbstractUser):
    date_of_birth = models.DateField(null=True)
    skin_type = models.ForeignKey(SkinType, on_delete=models.CASCADE, null=True)
    favorite_products = models.ManyToManyField(Product, related_name="members")

    class Meta:
        verbose_name = "member"
        verbose_name_plural = "members"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("cosmetics:member-detail", kwargs={"pk": self.pk})
