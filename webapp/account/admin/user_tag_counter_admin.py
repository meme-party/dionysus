from account.models import UserTagCounter
from django.contrib import admin
from unfold.admin import ModelAdmin


@admin.register(UserTagCounter)
class UserTagCounterAdmin(ModelAdmin):
    list_display = (
        "user",
        "tag",
        "bookmarks_count",
        "bookmarkings_count",
    )
    search_fields = (
        "user__email",
        "tag__name",
    )
    list_filter = (
        "user",
        "tag",
    )
    readonly_fields = (
        "user",
        "tag",
        "bookmarks_count",
        "bookmarkings_count",
    )
    fieldsets = (
        (
            "User Tag Counter",
            {
                "fields": (
                    "user",
                    "tag",
                    "bookmarks_count",
                    "bookmarkings_count",
                )
            },
        ),
    )
    actions = []
    ordering = (
        "user",
        "tag",
    )
    list_per_page = 20
    list_max_show_all = 200
