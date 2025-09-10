from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from studio.models import Sticker
from unfold.admin import ModelAdmin


@admin.register(Sticker)
class StickerAdmin(ModelAdmin):
    list_display = ("name", "ticket_price", "active", "created_at")
    list_filter = ("ticket_price", "created_at", "updated_at")
    search_fields = ("name", "description")
    ordering = ("-created_at", "name")

    fields = [
        "name",
        "image",
        "description",
        "ticket_price",
        "active",
        "active_at",
        "inactive_at",
        "creator",
        "created_at",
        "updated_at",
    ]

    readonly_fields = ["active", "active_at", "inactive_at", "created_at", "updated_at"]

    def activate_stickers(self, request, queryset):
        queryset.bulk_activate()
        self.message_user(request, _("Selected stickers have been activated."))

    def inactivate_stickers(self, request, queryset):
        queryset.bulk_inactivate()
        self.message_user(request, _("Selected stickers have been inactivated."))

    activate_stickers.short_description = _("Activate stickers")
    inactivate_stickers.short_description = _("Inactivate stickers")

    actions = ["activate_stickers", "inactivate_stickers"]
