from django.views.generic.list import ListView

from boardApp.models import Achievement


class PageAchievementView(ListView):
    """View of page achievements."""

    queryset = Achievement.objects.all()
    template_name = 'boardApp/page-achiave.html'
    context_object_name = 'objects'