from django.contrib import admin
from file_manager.models.thumbnail import Thumbnail
from unfold.admin import ModelAdmin


@admin.register(Thumbnail)
class ThumbnailAdmin(ModelAdmin):
    list_display = ("id", "preview_image", "url", "file", "web_url")
    search_fields = ("web_url",)
    list_filter = ("file",)

    fields = ("file", "web_url", "url")
    readonly_fields = ("url",)
