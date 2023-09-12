from django.shortcuts import render
from .models import Brand, Product, SkinType, Member


def index(request):
    """View function for the home page of the site."""

    num_brands = Brand.objects.count()
    num_products = Product.objects.count()
    num_skin_types = SkinType.objects.count()
    num_members = Member.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_brands": num_brands,
        "num_products": num_products,
        "num_skin_types": num_skin_types,
        "num_members": num_members,
        "num_visits": num_visits + 1,
    }

    return render(request, "cosmetics/index.html", context=context)
