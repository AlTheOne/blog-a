from django.urls import path

from galleryApp.views import MainGalleryView, CategoryGalleryView


urlpatterns = [
    path('<slug:category>/', CategoryGalleryView.as_view(), name='cat-gallery'),
    path('', MainGalleryView.as_view(), name='main-gallery'),
]