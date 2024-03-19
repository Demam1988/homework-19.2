from django.urls import reverse_lazy, reverse
from django.views.generic import (CreateView, ListView, DetailView,
                                  DeleteView, UpdateView)
from pytils.translit import slugify

from blog.models import Note


# Create your views here.
class NoteCreateView(CreateView):
    model = Note
    fields = [
        'header',
        'slug',
        'content',
        'preview',
        'is_published',
    ]
    success_url = reverse_lazy('blog:list')

    # (django_env)
    # andrejskovorodnikov @ MacBook - Air - Andrej
    # hello_django_19_2 % pip
    # install
    # pytils

    def form_valid(self, form):
        if form.is_valid():
            new_note = form.save()
            new_note.slug = slugify(new_note.header)
            new_note.save()

        return super().form_valid(form)


class NoteUpdateView(UpdateView):
    model = Note
    fields = [
        'header',
        'slug',
        'content',
        'preview',
        'is_published',
    ]

    def form_valid(self, form):
        if form.is_valid():
            new_note = form.save()
            new_note.slug = slugify(new_note.header)
            new_note.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail_view', args=[self.kwargs.get('pk')])

    # success_url = reverse_lazy('blog:list')


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('blog:list')


class NoteListView(ListView):
    model = Note

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class NoteDetailView(DetailView):
    model = Note

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object