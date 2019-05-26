from django.urls import path

from boardApp.views import PageAchievementView


urlpatterns = [
    path('', PageAchievementView.as_view(), name='page-achiev'),
]
