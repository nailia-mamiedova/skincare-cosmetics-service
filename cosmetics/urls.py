from django.urls import path
from .views import (
    index,
    restricted_view,
    BrandListView,
    BrandCreateView,
    BrandUpdateView,
    BrandDeleteView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("restricted/", restricted_view, name="restricted"),
    path("brands/", BrandListView.as_view(), name="brand-list"),
    path("brands/create/", BrandCreateView.as_view(), name="brand-create"),
    path("brands/<int:pk>/update/", BrandUpdateView.as_view(), name="brand-update"),
    path("brands/<int:pk>/delete/", BrandDeleteView.as_view(), name="brand-delete"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
]

app_name = "cosmetics"
