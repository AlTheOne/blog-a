from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from mbaseApp.models import *


class MainMbaseView(ListView):
    """View of main page articles."""

    queryset = Article.objects.defer('content').filter(is_active=True,
            category__is_active=True)
    template_name = 'mbaseApp/mbase-main.html'
    context_object_name = 'objects'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.filter(is_active=True)
        return context


class CategoryMbaseView(ListView):
    """View of pages catigories articles and related entries."""

    model = Article
    template_name = 'mbaseApp/mbase-main.html'
    context_object_name = 'objects'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.defer('content').filter(
            category__slug=self.kwargs.get('category'),
            is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.filter(is_active=True)
        return context


class PageMbaseView(DetailView):
    """Page detail of articles."""

    template_name = 'mbaseApp/page-mbase.html'
    context_object_name = 'objects'
    slug_name = 'slug'

    def get_object(self, category=None, id=None, *args, **kwargs):
        obj = get_object_or_404(
            Article,
            id=self.kwargs.get('id'),
            category__slug=self.kwargs.get('category'),
            category__is_active=True,
            is_active=True
        )

        obj_hits = HitsPage.objects.get(article=obj)
        obj_hits.hits = int(obj_hits.hits) + 1
        obj_hits.save()

        return obj

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.filter(is_active=True)
        return context