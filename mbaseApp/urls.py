from django.urls import path

from mbaseApp.views import (MainMbaseView, CategoryMbaseView,
    PageMbaseView)


urlpatterns = [
    path('<slug:category>/<int:id>/', PageMbaseView.as_view(), name='page-mbase'),
    path('<slug:category>/', CategoryMbaseView.as_view(), name='cat-mbase'),
    path('', MainMbaseView.as_view(), name='main-mbase'),
]