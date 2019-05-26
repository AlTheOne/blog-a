from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NbaseappConfig(AppConfig):
    name = 'nbaseApp'
    verbose_name = _("Нормативная база")