from django.contrib import admin

from Product.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category",)
    list_filter = ("category",)
    search_fields = ("name", "category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "pk",)
