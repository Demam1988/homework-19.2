from django.core.cache import cache

from catalog.models import Product
from config import settings


def get_categories():
    """Получает значения из кеша для отображения списка категорий"""
    product_list = cache.get('product_list')
    if product_list is None:
        product_list = Product.objects.all()
        cache.set('product_list', product_list, 60)
    return product_list
