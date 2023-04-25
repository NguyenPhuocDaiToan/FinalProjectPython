from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.objects.prefetch_related('product_image').filter(is_active=True)
    return render(request, "store/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(slug=category_slug).get_descendants(include_self=True)
    )
    # products = []
    return render(request, "store/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product.objects.prefetch_related('product_specification'), slug=slug)
    descriptions = product.description.split("\r\n", -1)
    return render(request, "store/single.html", {"product": product, "descriptions": descriptions})
