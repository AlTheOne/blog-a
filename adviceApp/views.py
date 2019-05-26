from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from adviceApp.models import *


class AdvicesListView(ListView):
    """View of main page list advices."""

    queryset = Advice.objects.all()
    template_name = 'adviceApp/advice-list.html'
    context_object_name = 'objects'
    paginate_by = 30

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.all()
        return context


class CategoryAdviceView(ListView):
    """View of pages catigories advices and related entries."""

    model = Advice
    template_name = 'adviceApp/advice-list.html'
    context_object_name = 'objects'
    paginate_by = 30

    def get_queryset(self):
        return Advice.objects.filter(category__slug=self.kwargs.get('category'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.all()
        return context