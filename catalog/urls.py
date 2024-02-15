from django.urls import path
from catalog.views import home, contacts

urlpatterns = [
    path('', home, name='catalog'),
    path('contacts/', contacts, name='catalog')
]