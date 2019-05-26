from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from pytils.translit import slugify


class Categories(models.Model):
    """Categories of module Advice."""

    title = models.CharField(
        max_length=120,
        unique=True,
        verbose_name=_('Название категории'),
        help_text=_('Не более 120 символов')
    )
    slug = models.SlugField(
        verbose_name=_('Ссылка'),
        unique=True,
        blank=True,
        max_length=128,
        help_text=_('Только латинские буквы, цифры и -, _. Не более 128 символов')
    )
    created = models.DateTimeField(
        verbose_name=_('Создано'),
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name=_('Обновлено'),
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Categories, self).save(*args, **kwargs)


class Advice(models.Model):
    """Advice for parents."""

    category = models.ForeignKey(
        Categories,
        verbose_name=_('Категория'),
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=255,
        unique=True,
        help_text=_('Не более 255 символов')
    )
    link = models.URLField(
        verbose_name=_('Прямая ссылка'),
        max_length=255,
        help_text=_('Не более 255 символов'),
        null=True,
        blank=True
    )
    myfile = models.FileField(
        verbose_name=_('Загрузить файл'),
        max_length=255,
        upload_to='adviceApp/files/',
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        verbose_name=_('Создано'),
        auto_now_add=True,
        auto_now = False
    )
    updated = models.DateTimeField(
        verbose_name=_('Обновлено'),
        auto_now_add=False,
        auto_now = True
    )

    class Meta:
        verbose_name = _('Рекомендация родителям')
        verbose_name_plural = _('Рекомендации родителям')
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Edit data myfile -> delete old file from HDD and upload new
        Condition: at least one field must be filled
        """
        if self.link or self.myfile is not None:
            if self.pk is not None:
                old_self = Advice.objects.get(pk=self.pk)
                if old_self.myfile and self.myfile != old_self.myfile:
                    old_self.myfile.delete(False)
        else:
            raise ValueError('Должно быть заполнено одно из полей: \
                Прямая ссылка или Загрузить файл')

        return super(Advice, self).save(*args, **kwargs)


@receiver(post_delete, sender = Advice)
def freezer_post_delete_handler(sender, **kwargs):
    """If deleted record => deleted file from HDD."""
    freezer = kwargs['instance']
    if freezer.myfile != '':
        storage, path = freezer.myfile.storage, freezer.myfile.path
        storage.delete(path)