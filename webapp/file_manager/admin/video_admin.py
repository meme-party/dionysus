from django.contrib import admin
from file_manager.models import Video
from unfold.admin import ModelAdmin


@admin.register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ("name", "file")
    search_fields = (
        "file",
        "name",
    )
    list_filter = ("file",)

    fields = (
        "name",
        "file",
    )
    readonly_fields = ()
