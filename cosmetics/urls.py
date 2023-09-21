from django.urls import path
from .views import index, restricted_view, BrandListView

urlpatterns = [
    path("", index, name="index"),
    path("restricted/", restricted_view, name="restricted"),
    path("brands/", BrandListView.as_view(), name="brand-list"),
]

app_name = "cosmetics"
