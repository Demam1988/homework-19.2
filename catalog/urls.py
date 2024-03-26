from django.conf import settings
from django.conf.urls.static import static
from django.db.models import PositiveIntegerField
from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
                  path('', ProductListView.as_view(), name='product_list'),
                  path('products', ProductListView.as_view(), name='product_list'),
                  path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
                  path('create/', ProductCreateView.as_view(), name='product_create'),
                  path('update/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
                  path('delete/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
