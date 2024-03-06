from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.models import Product, Category
from catalog.views import home, contacts, product_list, product_detail

urlpatterns = [
    path('', home, name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('contacts/', Category, name='category'),
    path('contacts/', Product, name='products'),
    path('', product_list, name='product_list'),
#    path('catalog/<pk:int>/', product_detail, name='product_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



