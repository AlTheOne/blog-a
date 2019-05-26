from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from tinymce import HTMLField


class StaticPages(models.Model):
    """Represents static pages, published on the web-site."""

    title = models.CharField(
        verbose_name=_('Заголовок страницы'),
        unique=True,
        max_length=120,
        help_text=_('Не более 120 символов')
    )
    slug = models.SlugField(
        verbose_name=_('Ссылка'),
        unique=True,
        max_length=128,
        help_text=_('Только латинские буквы, цифры и -, _. Не более 128 символов')
    )
    content = HTMLField('Описание',)
    is_active = models.BooleanField(
        verbose_name=_('Активировать'),
        default=True
    )
    created = models.DateTimeField(
        verbose_name=_('Дата создания'),
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name=_('Дата обновления'),
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        verbose_name = _('Статическая страница')
        verbose_name_plural = _('Статические страницы')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('static-page', args=[str(self.slug)])