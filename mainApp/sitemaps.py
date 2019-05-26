from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from mainApp.models import StaticPages


class MainPageSitemap(Sitemap):
    """Class for generate record main page sitemape."""

    changefreq = "daily"
    priority = 1

    def items(self):
        return ['main']

    def location(self, item):
        return reverse(item)


class ProtfolioSitemap(Sitemap):
    """Class for generate record portfolio sitemape."""

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return StaticPages.objects.filter(slug='portfolio')