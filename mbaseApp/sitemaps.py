from django.contrib.sitemaps import Sitemap
from mbaseApp.models import Article


class ArticlesSitemap(Sitemap):
    """Class for generate sitemape of module Articles."""
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Article.objects.filter(is_active=True, category__is_active=True)

    def lastmod(self, obj):
        return obj.updated