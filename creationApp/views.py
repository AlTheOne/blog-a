from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from creationApp.models import *


class MainCreationView(ListView):
    """View of main page creation."""

    queryset = Creation.objects.defer('content').filter(is_active=True,
            category__is_active=True)
    template_name = 'creationApp/creation-main.html'
    context_object_name = 'objects'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.filter(is_active=True)
        return context


class CategoryCreationView(ListView):
    """View of pages catigories creation and related entries."""

    model = Creation
    template_name = 'creationApp/creation-main.html'
    context_object_name = 'objects'
    paginate_by = 5

    def get_queryset(self):
        return Creation.objects.defer('content').filter(
            category__slug=self.kwargs.get('category'),
            is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.filter(is_active=True)
        return context


class PageCreationView(DetailView):
    """Page detail of creations."""

    template_name = 'creationApp/page-creation.html'
    context_object_name = 'objects'
    slug_name = 'slug'

    def get_object(self):
        obj = get_object_or_404(
            Creation,
            id=self.kwargs.get('id'),
            category__slug=self.kwargs.get('category'),
            category__is_active=True,
            is_active=True
        )

        obj_hits = HitsPage.objects.get(creation=obj)
        obj_hits.hits = int(obj_hits.hits) + 1
        obj_hits.save()

        return obj

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.filter(is_active=True)
        return context