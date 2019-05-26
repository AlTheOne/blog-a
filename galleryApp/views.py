from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from galleryApp.models import *


class MainGalleryView(ListView):
    """View of main page Gallery."""

    queryset = Images.objects.filter(is_active=True, category__is_active=True)
    template_name = 'galleryApp/gallery-main.html'
    context_object_name = 'objects'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.filter(is_active=True)
        return context


class CategoryGalleryView(ListView):
    """View of pages catigories creation and related entries."""

    model = Images
    template_name = 'galleryApp/gallery-main.html'
    context_object_name = 'objects'
    paginate_by = 20

    def get_queryset(self):
        return Images.objects.filter(
            category__slug=self.kwargs.get('category'),
            is_active=True
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Categories.objects.filter(is_active=True)
        return context


# class MainGallery(View, Pagination):
#     TEMPLATE = 'galleryApp/gallery-main.html'
#     QS = None

#     def get(self, *args, **kwargs):
#         data = {}

#         self.QS = Images.objects.filter(is_active = True, 
#             category__is_active = True)

#         data['categories'] = Categories.objects.filter(is_active = True)
#         data['paginator'] = self.mainPaginator(20)
#         data['objects'] = self.QS
#         return render(self.request, self.TEMPLATE, context = data)


# class CategoryGallery(View, Pagination):
#     TEMPLATE = 'galleryApp/gallery-main.html'
#     QS = None

#     def get(self, *args, **kwargs):
#         data = {}

#         data['category'] = get_object_or_404(Categories, 
#             slug=kwargs.get('category'), is_active = True)
#         self.QS = Images.objects.filter(category__slug = kwargs.get('category'), 
#             is_active = True)

#         data['categories'] = Categories.objects.filter(is_active = True)
#         data['paginator'] = self.mainPaginator(20)
#         data['objects'] = self.QS
#         return render(self.request, self.TEMPLATE, context = data)