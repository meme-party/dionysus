from django.contrib import admin
from meme.models import Meme
from tag.models import MemeTagging
from unfold.admin import ModelAdmin, TabularInline


class MemeTaggingInline(TabularInline):
    model = MemeTagging
    extra = 1
    fields = ["tag"]


@admin.register(Meme)
class MemeAdmin(ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    list_filter = ("title",)
    search_fields = ("title", "description")
    ordering = ("-created_at", "title")
    inlines = [MemeTaggingInline]
    fields = [
        "title",
        "description",
        "original_link",
        "published_at",
        "archived_at",
        "creator",
        "created_at",
        "updated_at",
    ]

    exclude = ["deleted_at"]
    readonly_fields = ["created_at", "updated_at", "deleted_at"]


# TODO: publish 액션, published_at에 시간 넣기
# TODO: archive 액션, archived_at에 시간 넣기
