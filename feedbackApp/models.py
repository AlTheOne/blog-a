from django.db import models
from django.utils.translation import ugettext_lazy as _


class FeedBackMessages(models.Model):
    """Represents feedback messages."""

    name = models.CharField(
        verbose_name=_('Имя отправителя'),
        max_length=100,
        blank=True,
        help_text=_('Не более 100 символов')
    )
    email = models.EmailField(
        verbose_name=_('Почта отправителя'),
        max_length=254,
        help_text=_('Не более 100 символов')
    )
    phone = models.CharField(
        verbose_name=_('Телефон отправителя'),
        max_length=25,
        blank=True,
        help_text=_('Не более 25 символов')
    )
    message = models.TextField(verbose_name=_('Сообщение'))
    created = models.DateTimeField(
        verbose_name=_('Получено'),
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        verbose_name = _('Обратная связь')
        verbose_name_plural = _('Обратная связь')
        ordering = ['-created']

    def __str__(self):
        return self.email