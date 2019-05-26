from django.contrib import admin
from mainApp.models import *


@admin.register(StaticPages)
class StaticPagesAdmin(admin.ModelAdmin):
    """Showing entity model StaticPages."""

    list_display = ('id', 'title', 'slug', 'is_active', 'updated', 'created')
    list_display_links = ('id', 'title')
    fields = ('title', 'slug', 'content', 'is_active', ('updated', 'created'))
    readonly_fields = ('updated', 'created')
    search_fields = ('title', 'content')