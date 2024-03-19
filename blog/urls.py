from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import (NoteListView, NoteDetailView, NoteCreateView,
                        NoteDeleteView, NoteUpdateView)

app_name = 'blog'

urlpatterns = [
                  path('', NoteListView.as_view(), name='list'),
                  path('create/', NoteCreateView.as_view(),
                       name='create'),
                  path('view/<int:pk>/', NoteDetailView.as_view(),
                       name='detail_view'),
                  path('delete/<int:pk>', NoteDeleteView.as_view(),
                       name='delete'),
                  path('edit/<int:pk>', NoteUpdateView.as_view(), name='edit'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)