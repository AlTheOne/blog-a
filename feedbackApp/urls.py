from django.urls import path

from feedbackApp.views import *


urlpatterns = [
    path('', FeedBackView.as_view(), name='feedback'),
]