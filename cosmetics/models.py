from django.db import models
from django.contrib.auth.models import AbstractUser


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)


class SkinType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    skin_types = models.ManyToManyField(SkinType, related_name="products")
    ingredients = models.TextField()
    description = models.TextField()


class Member(AbstractUser):
    date_of_birth = models.DateField(null=True)
    skin_type = models.ForeignKey(SkinType, on_delete=models.CASCADE, null=True)
    favorite_products = models.ManyToManyField(Product, related_name="members")
