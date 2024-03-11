
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


# Create your views here.
def home(request):
    return render(request, 'catalog/base.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'image', 'description', 'price')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'image')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')




# def product_list(request):
#     """Выдает список со всеми продуктами"""
#     product = Product.objects.all()
#     context = {
#         'objects_list': product
#     }
#
#     return render(request, 'catalog/product_list.html', context)


# def product_detail(request, pk):
#     """Выдает список с продуктам по рк."""
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product
#     }
#
#     return render(request, 'catalog/product_detail.html', context)


