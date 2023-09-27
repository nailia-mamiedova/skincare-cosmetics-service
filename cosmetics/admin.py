from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Brand, SkinType, Product, Member


@admin.register(Member)
class MemberAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("date_of_birth", "skin_type")
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": (
            "date_of_birth",
            "skin_type",
            "favorite_products"
        )}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "date_of_birth",
                        "skin_type",
                        "favorite_products",
                    )
                },
            ),
        )
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("country",)


@admin.register(SkinType)
class SkinTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = (
        "brand__name",
        "skin_types",
    )
