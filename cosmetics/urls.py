from django.urls import path
from .views import (
    index,
    restricted_view,
    BrandListView,
    BrandCreateView,
    BrandUpdateView,
    BrandDeleteView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    add_remove_favorite,
    SkinTypeListView,
    SkinTypeCreateView,
    SkinTypeUpdateView,
    SkinTypeDeleteView,
    MemberListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("restricted/", restricted_view, name="restricted"),
    path("brands/", BrandListView.as_view(), name="brand-list"),
    path("brands/create/", BrandCreateView.as_view(), name="brand-create"),
    path("brands/<int:pk>/update/", BrandUpdateView.as_view(), name="brand-update"),
    path("brands/<int:pk>/delete/", BrandDeleteView.as_view(), name="brand-delete"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/detail/", ProductDetailView.as_view(), name="product-detail"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    path("products/<int:pk>/add_favorite/", add_remove_favorite, name="add-remove-favorite"),
    path("skin_types/", SkinTypeListView.as_view(), name="skin-type-list"),
    path("skin_types/create/", SkinTypeCreateView.as_view(), name="skin-type-create"),
    path("skin_types/<int:pk>/update/", SkinTypeUpdateView.as_view(), name="skin-type-update"),
    path("skin_types/<int:pk>/delete/", SkinTypeDeleteView.as_view(), name="skin-type-delete"),
    path("members/", MemberListView.as_view(), name="member-list"),
]

app_name = "cosmetics"
