from django.contrib import admin
from mbaseApp.models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Showing entity model Categories."""

    list_display = ('title', 'is_active', 'created')
    list_display_links = ('title',)
    readonly_fields = ('updated', 'created')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Showing entity model Articles."""

    list_display = ('id', 'title', 'category', 'is_active', 'updated', 'created')
    list_display_links = ('id', 'title')
    fields = ('category', 'title', ('image', 'preview'), 'description', 'content', 'is_active', ('updated', 'created'))
    readonly_fields = ('preview', 'updated', 'created')
    search_fields = ('title', 'content')


@admin.register(HitsPage)
class HitsPageAdmin(admin.ModelAdmin):
    """Showing entity model HitsPage."""

    list_display = ('article', 'hits')
    readonly_fields = ('article', 'hits')

    def has_delete_permission(self, request, obj=None):
        return False