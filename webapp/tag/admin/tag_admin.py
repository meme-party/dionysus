from django.contrib import admin
from tag.models import Tag
from unfold.admin import ModelAdmin


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "updated_at",
    )
    list_filter = ("name", "category")
    search_fields = ()
    ordering = ()

    exclude = ["deleted_at"]
    readonly_fields = [
        "split_name",
        "first_letter",
        "created_at",
        "updated_at",
        "deleted_at",
    ]

    fields = (
        "name",
        "split_name",
        "first_letter",
        "description",
        "category",
        "created_at",
        "updated_at",
    )
