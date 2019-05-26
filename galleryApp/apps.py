from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GalleryappConfig(AppConfig):
    name = 'galleryApp'
    verbose_name = _("Галерея")