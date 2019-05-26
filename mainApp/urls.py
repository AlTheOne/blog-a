from django.urls import path

from mainApp.views import MainView, StaticPageView


urlpatterns = [
    path('<slug:page>/', StaticPageView.as_view(), name='static-page'),
    path('', MainView.as_view(), name='main'),
]