import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.validators import FileExtensionValidator

from pytils.translit import slugify
from PIL import Image


class Categories(models.Model):
    """Categories of module Images."""

    title = models.CharField(
        verbose_name=_('Название категории'),
        unique=True,
        max_length=120,
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


class Images(models.Model):
    """Represents gallery, published on the web-site."""

    category = models.ForeignKey(
        Categories,
        verbose_name=_('Категория'),
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
        unique=True,
        max_length=120,
        help_text=_('Не более 120 символов')
    )
    is_active = models.BooleanField(
        verbose_name=_('Активировать'),
        default=True
    )
    preview = models.ImageField(
        upload_to='galleryApp/preview/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ],
        verbose_name=_('Превью'),
        null = True,
        blank=True,
        help_text=_('Заполняется автоматически')
    )
    image = models.ImageField(
        upload_to='galleryApp/preview/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ],
        verbose_name=_('Изображение'),
        help_text=_('Допустимые форматы: JPG, JPEG, PNG')
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
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')
        ordering = ['-created']

    def __str__(self):
        return self.title

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
                thumbname = filename + "_" + str(size['width']) + \
                            "x" + str(size['height']) + '.' + extension
                im.save(fullpath + os.sep + thumbname)
                self.preview = images_thumb_name(self, thumbname)


        if self.pk is not None:
            old_self = Images.objects.get(pk=self.pk)
            if old_self.image and self.image != old_self.image:
                old_self.image.delete(False)
                old_self.preview.delete(False)
                super(Images, self).save(*args, **kwargs)
                did_thumbimg()

        else:
            super(Images, self).save(*args, **kwargs)
            did_thumbimg()
        return super(Images, self).save(*args, **kwargs)


@receiver(post_delete, sender = Images)
def freezer_post_delete_handler(sender, **kwargs):
    """If deleted record => deleted preview and image from HDD."""
    freezer = kwargs['instance']
    storage, path = freezer.image.storage, freezer.image.path
    storage_preview, path_preview = freezer.preview.storage, freezer.preview.path
    storage.delete(path)
    storage_preview.delete(path_preview)