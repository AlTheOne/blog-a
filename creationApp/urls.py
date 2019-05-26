from django.urls import path

from creationApp.views import (MainCreationView, CategoryCreationView,
                                PageCreationView)


urlpatterns = [
    path('<slug:category>/<int:id>/', PageCreationView.as_view(), name='page-creation'),
    path('<slug:category>/', CategoryCreationView.as_view(), name='cat-creation'),
    path('', MainCreationView.as_view(), name='main-creation'),
]