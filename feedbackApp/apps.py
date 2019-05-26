from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FeedbackappConfig(AppConfig):
    name = 'feedbackApp'
    verbose_name = _("Обратная связь")