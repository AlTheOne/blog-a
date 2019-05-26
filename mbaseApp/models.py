import os

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.validators import FileExtensionValidator

from pytils.translit import slugify
from tinymce import HTMLField
from PIL import Image


class Categories(models.Model):
    """Categories of module Articles."""

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
    is_active = models.BooleanField(
        verbose_name=_('Активировать'),
        default=True
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

class HitsPage(models.Model):
    """Number of views instance of Article."""

    article = models.OneToOneField(
        'Article',
        related_name='data_hit',
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_('Материал')
    )
    hits = models.IntegerField(verbose_name=_('Просмотров'), default=0)

    class Meta:
        verbose_name = _('Просмотры страницы')
        verbose_name_plural = _('Просмотры страниц')

    def __str__(self):
        return self.article.title


class Article(models.Model):
    """Represents artciles, published on the web-site."""

    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Категория'),
    )
    title = models.CharField(
        verbose_name=_('Название'),
        unique=True,
        max_length=120,
        help_text=_('Не более 120 символов'))
    description = models.TextField(
        max_length=150,
        verbose_name=_('Краткое описание'),
        help_text=_('Не более 150 символов')
    )
    content = HTMLField('Контент',)
    is_active = models.BooleanField(
        verbose_name=_('Активировать'),
        default=True
    )
    preview = models.ImageField(
        upload_to='mbaseApp/preview/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ],
        verbose_name=_('Превью'),
        null=True,
        blank=True,
        help_text=_('Заполняется автоматически')
    )
    image = models.ImageField(
        upload_to='mbaseApp/preview/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ],
        verbose_name=_('Картинка')
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
        verbose_name = _('Методический материал')
        verbose_name_plural = _('Методические материалы')
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page-mbase', args=[str(self.category.slug), str(self.id)])

    def get_thumb_image_url(self):
        """Get URL thumb_image."""
        return MEDIA_URL + self.preview

    def save(self, *args, **kwargs):
        """Function 'did_thumbimg' use Pillow."""
        size = {'height': 300, 'width': 300}

        def did_thumbimg():
            def images_thumb_name(instance, filename):
                original_image_path = str(instance.image).rsplit('/', 1)[0]
                return os.path.join(original_image_path, filename).replace('\\', '/')

            extension = str(self.image.path).rsplit('.', 1)[1]
            filename = str(self.image.path).rsplit(os.sep, 1)[1].rsplit('.', 1)[0]
            fullpath = str(self.image.path).rsplit(os.sep, 1)[0]

            if extension in ['jpg', 'jpeg', 'png']:
                im = Image.open(str(self.image.path))
                im.thumbnail((size['width'], size['height']))
                thumbname = filename + "_" + str(size['width']) + "x" + \
                            str(size['height']) + '.' + extension
                im.save(fullpath + os.sep + thumbname)
                self.preview = images_thumb_name(self, thumbname)


        if self.pk is not None:
            old_self = Article.objects.get(pk=self.pk)
            if old_self.image and self.image != old_self.image:
                old_self.image.delete(False)
                old_self.preview.delete(False)
                super(Article, self).save(*args, **kwargs)
                did_thumbimg()

        else:
            super(Article, self).save(*args, **kwargs)
            did_thumbimg()
        return super(Article, self).save(*args, **kwargs)


@receiver(post_save, sender = Article)
def save_counter_article(sender, **kwargs):
    """If new instance created than create record for counter."""
    try:
        HitsPage.objects.get(article=kwargs['instance'])
    except HitsPage.DoesNotExist:
        obj = HitsPage.objects.create(article=kwargs['instance'])
        obj.save()


@receiver(post_delete, sender = Article)
def freezer_post_delete_handler(sender, **kwargs):
    """If deleted record => deleted preview and image from HDD."""
    freezer = kwargs['instance']
    storage, path = freezer.image.storage, freezer.image.path
    storage_preview, path_preview = freezer.preview.storage, freezer.preview.path
    storage.delete(path)
    storage_preview.delete(path_preview)