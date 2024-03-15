from django.contrib.auth.mixins import LoginRequiredMixin
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
    template_name = "catalog/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
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


