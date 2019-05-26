from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CreationappConfig(AppConfig):
    name = 'creationApp'
    verbose_name = _("Моё творчество")