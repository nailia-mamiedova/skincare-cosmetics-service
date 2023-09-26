from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    BrandSearchForm,
    ProductSearchForm,
    SkinTypeSearchForm,
    MemberSearchForm,
    MemberCreationForm,
)
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


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    queryset = Product.objects.all()


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


class SkinTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = SkinType
    fields = "__all__"
    template_name = "cosmetics/skin_type_form.html"
    success_url = reverse_lazy("cosmetics:skin-type-list")


class SkinTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = SkinType
    fields = "__all__"
    template_name = "cosmetics/skin_type_form.html"
    success_url = reverse_lazy("cosmetics:skin-type-list")


class SkinTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = SkinType
    template_name = "cosmetics/skin_type_confirm_delete.html"
    success_url = reverse_lazy("cosmetics:skin-type-list")


class MemberListView(LoginRequiredMixin, generic.ListView):
    model = Member
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = MemberSearchForm(initial={
            "username": username,
        })

        return context

    def get_queryset(self):
        queryset = Member.objects.all()
        form = MemberSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"],
            )

        return queryset


class MemberCreateView(LoginRequiredMixin, generic.CreateView):
    model = Member
    form_class = MemberCreationForm


@login_required
def add_remove_favorite(request, pk):
    member = Member.objects.get(id=request.user.id)
    if (
        Product.objects.get(id=pk) in member.favorite_products.all()
    ):
        member.favorite_products.remove(pk)
    else:
        member.favorite_products.add(pk)
    return HttpResponseRedirect(reverse_lazy("cosmetics:product-detail", args=[pk]))


def restricted_view(request):
    return render(request, 'cosmetics/restricted.html')
