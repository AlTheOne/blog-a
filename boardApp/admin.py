from django.contrib import admin
from boardApp.models import *


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """Showing entity model Achievement."""

    list_display = ('id', 'title', 'type_achiav', 'updated', 'created')
    list_display_links = ('id', 'title')
    fields = ('type_achiav', 'title', ('image', 'preview'), ('updated', 'created'))
    readonly_fields = ('preview', 'updated', 'created')
    list_filter = ('type_achiav',)
    search_fields = ('title',)