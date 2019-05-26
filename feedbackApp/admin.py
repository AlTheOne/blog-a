from django.contrib import admin

from feedbackApp.models import FeedBackMessages


@admin.register(FeedBackMessages)
class FeedBackMessagesAdmin(admin.ModelAdmin):
    """Showing entity model FeedBackMessages."""

    list_display = ('id', 'email', 'name', 'phone', 'created')
    list_display_links = ('id', 'email')
    readonly_fields = ('email', 'name', 'phone', 'message', 'created')