from django.contrib import admin
from galleryApp.models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Showing entity model Categories."""

    list_display = ('title', 'is_active', 'created')
    list_display_links = ('title',)
    readonly_fields = ('updated', 'created')


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    """Showing entity model Images."""

    list_display = ('id', 'title', 'category', 'is_active', 'updated', 'created')
    list_display_links = ('id', 'title')
    fields = (
        'category',
        'title',
        ('image', 'preview'),
        'is_active',
        ('updated', 'created')
    )
    readonly_fields = ('preview', 'updated', 'created')
    search_fields = ('title',)
    list_filter = ('category', 'is_active')