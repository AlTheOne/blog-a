from django.urls import path

from nbaseApp.views import NbaseListView


urlpatterns = [
    path('', NbaseListView.as_view(), name='main-nbase'),
]