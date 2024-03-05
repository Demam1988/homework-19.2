from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.models import Product, Category
from catalog.views import home, contacts, base_list

urlpatterns = [
    path('', home, name='catalog'),
    path('contacts/', contacts, name='catalog'),
    path('contacts/', Category, name='category'),
    path('products/', Product, name='products'),
    path('', base_list, name='base_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

