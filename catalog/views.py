from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


def home(request):
    return render(request, 'catalog/base.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"


# class BlogCreateView(CreateView):
#         model = Blog
#         fields = (
#             'title', 'content', 'img_preview',
#             'sign_publication',)  # здесь устанавливаются поля для автоматической формы
#         success_url = reverse_lazy('catalog:blog_list')
#
#         def form_valid(self, form):
#             if form.is_valid():
#                 new_blog = form.save()
#                 new_blog.slug = slugify(new_blog.title)
#                 new_blog.save()
#             return super().form_valid(form)
#
#
# class BlogListView(ListView):
#         model = Blog
#
#         def get_queryset(self, *args, **kwargs):
#             queryset = super().get_queryset(*args, **kwargs)
#             queryset = queryset.filter(sign_publication=True)
#             return queryset
#
#
# class BlogDetailView(DetailView):
#         model = Blog
#         success_url = reverse_lazy('catalog:blog_list')
#
#         def get_object(self, queryset=None):
#             """ добавили счетик просмотров """
#             self.object = super().get_object(queryset)
#             self.object.number_views += 1
#             self.object.save()
#             return self.object
#
#
# class BlogUpdateView(UpdateView):
#     model = Blog
#     fields = ('title', 'slug', 'content', 'img_preview', 'sign_publication', 'number_views',)
#     success_url = reverse_lazy('catalog:blog_list')
#
#
# class BlogDeleteView(DeleteView):
#     model = Blog
#     success_url = reverse_lazy('catalog:blog_list')
#

###################################################################
# crud для продуктов
###################################################################


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
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

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
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
