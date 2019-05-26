from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.detail import DetailView
from django.template import RequestContext

from mainApp.models import StaticPages


class MainView(DetailView):
    """Main page on site."""

    template_name = 'mainApp/static-page.html'
    context_object_name = 'objects'
    slug_name = 'slug'

    def get_object(self):
        obj = get_object_or_404(
            StaticPages,
            slug='main',
            is_active=True
        )

        return obj


class StaticPageView(DetailView):
    """Static page on site."""

    template_name = 'mainApp/static-page.html'
    context_object_name = 'objects'
    slug_name = 'page'

    def get_object(self):
        obj = get_object_or_404(
            StaticPages,
            slug=self.kwargs.get('page'),
            is_active=True
        )

        return obj


def e_handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response


def e_handler500(request, *args, **kwargs):
    response = render_to_response(
        '500.html',
        {},
        context_instance=RequestContext(request)
    )
    response.status_code = 500
    return response