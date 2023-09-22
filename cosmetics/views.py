from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .forms import BrandSearchForm, ProductSearchForm
from .models import Brand, Product, SkinType, Member


@login_required
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


class BrandListView(LoginRequiredMixin, generic.ListView):
    model = Brand
    context_object_name = "brand_list"
    template_name = "cosmetics/brand_list.html"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = BrandSearchForm(initial={
            "name": name,
        })

        return context

    def get_queryset(self):
        queryset = Brand.objects.all()
        form = BrandSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"],
            )

        return queryset


class BrandCreateView(LoginRequiredMixin, generic.CreateView):
    model = Brand
    fields = "__all__"
    template_name = "cosmetics/brand_form.html"
    success_url = "/brands/"


class BrandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Brand
    fields = "__all__"
    template_name = "cosmetics/brand_form.html"
    success_url = "/brands/"


class BrandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Brand
    template_name = "cosmetics/brand_confirm_delete.html"
    success_url = "/cosmetics/brands/"


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "cosmetics/product_list.html"
    paginate_by = 8


def restricted_view(request):
    return render(request, 'cosmetics/restricted.html')
