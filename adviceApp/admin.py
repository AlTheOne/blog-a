from django.contrib import admin
from adviceApp.models import Advice, Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Showing entity model Categories."""

    list_display = ('title', 'created')
    list_display_links = ('title',)
    readonly_fields = ('updated', 'created')


@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    """Showing entity model Advices."""

    list_display = ('id', 'title', 'updated', 'created')
    list_display_links = ('id', 'title')