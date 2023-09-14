from django.urls import path
from .views import index, restricted_view


urlpatterns = [
    path("", index, name="index"),
    path("restricted/", restricted_view, name="restricted"),
]

app_name = "cosmetics"
