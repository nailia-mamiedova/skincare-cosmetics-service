from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import BrandSearchForm, ProductSearchForm, SkinTypeSearchForm
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
    success_url = reverse_lazy("cosmetics:brand-list")


class BrandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy("cosmetics:brand-list")


class BrandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Brand
    success_url = reverse_lazy("cosmetics:brand-list")


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = ProductSearchForm(initial={
            "name": name,
        })

        return context

    def get_queryset(self):
        queryset = Product.objects.all()
        form = ProductSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"],
            )

        return queryset


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("cosmetics:product-list")


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("cosmetics:product-list")


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy("cosmetics:product-list")


class SkinTypeListView(LoginRequiredMixin, generic.ListView):
    model = SkinType
    context_object_name = "skin_type_list"
    template_name = "cosmetics/skin_type_list.html"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SkinTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = SkinTypeSearchForm(initial={
            "name": name,
        })

        return context

    def get_queryset(self):
        queryset = SkinType.objects.all()
        form = SkinTypeSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"],
            )

        return queryset


def restricted_view(request):
    return render(request, 'cosmetics/restricted.html')
