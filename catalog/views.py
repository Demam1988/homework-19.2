from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.
def home(request):
    return render(request, 'catalog/base.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_list(request):
    """Выдает список со всеми продуктами"""
    product = Product.objects.all()
    context = {
        'objects_list': product
    }

    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    """Выдает список с продуктам по рк."""
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }

    return render(request, 'catalog/product_detail.html', context)


