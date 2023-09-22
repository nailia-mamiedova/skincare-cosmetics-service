from django.urls import path
from .views import (
    index,
    restricted_view,
    BrandListView,
    BrandCreateView,
    BrandUpdateView,
    BrandDeleteView,
    ProductListView
)

urlpatterns = [
    path("", index, name="index"),
    path("restricted/", restricted_view, name="restricted"),
    path("brands/", BrandListView.as_view(), name="brand-list"),
    path("brands/create/", BrandCreateView.as_view(), name="brand-create"),
    path("brands/<int:pk>/update/", BrandUpdateView.as_view(), name="brand-update"),
    path("brands/<int:pk>/delete/", BrandDeleteView.as_view(), name="brand-delete"),
    path("products/", ProductListView.as_view(), name="product-list"),
]

app_name = "cosmetics"
