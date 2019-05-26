from django.urls import path
from adviceApp.views import AdvicesListView, CategoryAdviceView


urlpatterns = [
    path('<slug:category>/', CategoryAdviceView.as_view(), name='cat-advice'),
    path('', AdvicesListView.as_view(), name='main-advice'),
]