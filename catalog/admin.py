from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category",)
    list_filter = ("category",)
    search_fields = ("name", "category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "pk",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "name_ver", "number_ver",)
    list_filter = ("number_ver",)
    search_fields = ("name", "number_ver",)


# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'content', 'img_preview', 'sign_publication', 'number_views',)
