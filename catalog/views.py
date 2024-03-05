from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def base_list(request):
    product = Product.objects.all()
    context = {
        'objects_list': product
    }

    return render(request, 'catalog/product_list.html', context)


