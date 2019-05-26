from django.contrib import admin

from nbaseApp.models import Normative


@admin.register(Normative)
class NormativeAdmin(admin.ModelAdmin):
    """Showing entity model Normative."""

    list_display = ('id', 'title', 'updated', 'created')
    list_display_links = ('id', 'title')