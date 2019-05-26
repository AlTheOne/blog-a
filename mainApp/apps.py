from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MainappConfig(AppConfig):
    name = 'mainApp'
    verbose_name = _("Статические страницы")