from django.urls import path

from catalog.models import Product, Category
from catalog.views import home, contacts

urlpatterns = [
    path('', home, name='catalog'),
    path('contacts/', contacts, name='catalog'),
    path('contacts/', Category, name='category'),
    path('products/', Product, name='products'),
]
