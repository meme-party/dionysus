from django.contrib import admin
from meme.models import Meme, MemeCounter
from tag.models import MemeTagging
from unfold.admin import ModelAdmin, TabularInline


class MemeTaggingInline(TabularInline):
    model = MemeTagging
    extra = 1
    fields = ["tag"]


class MemeCounterInline(TabularInline):
    model = MemeCounter
    extra = 1
    fields = ["bookmarking_users_count", "bookmarkings_count"]
    readonly_fields = ["bookmarking_users_count", "bookmarkings_count"]


@admin.register(Meme)
class MemeAdmin(ModelAdmin):
    def reset_all_counters(self, request, queryset):
        for meme in queryset:
            meme.reset_all_counters()
        self.message_user(request, "All counters have been reset.")

    list_display = ("title", "type", "created_at", "updated_at")
    list_filter = ("title", "type")
    search_fields = ("title", "description")
    ordering = ("-created_at", "title")
    inlines = [MemeTaggingInline, MemeCounterInline]
    fields = [
        "title",
        "type",
        "thumbnail",
        "audio",
        "video",
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

    reset_all_counters.short_description = "Reset all counters"
    actions = ["reset_all_counters"]


# TODO: publish 액션, published_at에 시간 넣기
# TODO: archive 액션, archived_at에 시간 넣기
