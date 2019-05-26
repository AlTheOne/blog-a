from django.contrib import admin
from creationApp.models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Showing entity model Categories."""

    list_display = ('title', 'is_active', 'created')
    list_display_links = ('title',)
    readonly_fields = ('updated', 'created')


@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    """Showing entity model Creation."""

    list_display = ('id', 'title', 'category', 'is_active', 'updated', 'created')
    list_display_links = ('id', 'title')
    fields = (
        'category', 'title', ('image', 'preview'),
        'description', 'content', 'is_active', ('updated', 'created')
    )
    readonly_fields = ('preview', 'updated', 'created')
    search_fields = ('title', 'content')
    save_on_top = True


@admin.register(HitsPage)
class HitsPageAdmin(admin.ModelAdmin):
    """Showing entity model HitsPage."""

    list_display = ('creation', 'hits')
    readonly_fields = ('creation', 'hits')

    def has_delete_permission(self, request, obj=None):
        return False