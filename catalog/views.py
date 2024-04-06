from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version


def home(request):
    return render(request, 'catalog/base.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(category_id=self.kwargs.get('pk'))
        print(queryset[0].category)
        return queryset

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_list', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1, )
        if self.request.method == "POST":
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            # попытка сделать возможность редактирования только у авторизированных пользователей
            self.object = form.save()
            self.object.owner = self.request.user
            self.object.save()

            return super().form_valid(form)

    def get_form_class(self):
        """Переопределение метода выбора формы для редактирования"""
        user = self.request.user
        perms = ("product.change_published", "product.change_description", "product.change_category")
        if user.has_perms(perms):
            return ProductModeratorForm
        if user == self.object.owner:
            return ProductForm
        raise HttpResponseForbidden


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactView(View):
    template_name = "catalog/contacts.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, "catalog/not_available.html")
