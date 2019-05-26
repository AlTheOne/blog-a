from django.contrib.sitemaps import Sitemap
from creationApp.models import Creation


class CreationSitemap(Sitemap):
    """Class for generate sitemape of module Creation."""

    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Creation.objects.filter(is_active=True, category__is_active=True)

    def lastmod(self, obj):
        return obj.updated