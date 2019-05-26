from django.views.generic.list import ListView

from nbaseApp.models import *


class NbaseListView(ListView):
    """View of main page documents."""

    queryset = Normative.objects.all()
    template_name = 'nbaseApp/nbase-list.html'
    context_object_name = 'objects'