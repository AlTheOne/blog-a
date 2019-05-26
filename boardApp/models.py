import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.validators import FileExtensionValidator

from PIL import Image


TYPE_ACHIAVMENT_CHOICES = (
    ('personal', 'Личное'),
    ('student', 'Воспитанников'),
)

class Achievement(models.Model):
    """Achievement contain images of diplomas."""

    type_achiav = models.CharField(
        verbose_name=_('Тип достижения'),
        max_length=8,
        choices=TYPE_ACHIAVMENT_CHOICES
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=120,
        help_text=_('Не более 120 символов')
    )
    preview = models.ImageField(
        upload_to='boardApp/preview/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ],
        verbose_name=_('Превью'),
        null=True,
        blank=True,
        help_text=_('Заполняется автоматически')
    )
    image = models.ImageField(
        upload_to='boardApp/preview/',
        verbose_name=_('Изображение')
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
        verbose_name = _('Достижение')
        verbose_name_plural = _('Достижения')
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
                """Create path."""
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
            old_self = Achievement.objects.get(pk=self.pk)
            if old_self.image and self.image != old_self.image:
                old_self.image.delete(False)
                old_self.preview.delete(False)
                super(Achievement, self).save(*args, **kwargs)
                did_thumbimg()

        else:
            super(Achievement, self).save(*args, **kwargs)
            did_thumbimg()
        return super(Achievement, self).save(*args, **kwargs)


@receiver(post_delete, sender = Achievement)
def freezer_post_delete_handler(sender, **kwargs):
    """If deleted record => deleted preview and image from HDD."""
    freezer = kwargs['instance']
    storage, path = freezer.image.storage, freezer.image.path
    storage_preview, path_preview = freezer.preview.storage, freezer.preview.path
    storage.delete(path)
    storage_preview.delete(path_preview)