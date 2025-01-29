from bookmark.models.bookmark import Bookmark
from django.contrib import admin
from unfold.admin import ModelAdmin

# from django.utils.translation import gettext_lazy as _


class BookmarkAdmin(ModelAdmin):
    list_display = ("title", "user", "bookmarkings_count")
    search_fields = ("title", "user__username")
    list_filter = ("user",)
    readonly_fields = ("bookmarkings_count",)

    # def reset_bookmarkings_count(self, request, queryset):
    #     for bookmark in queryset:
    #         bookmark.reset_bookmarkings_count()
    #     self.message_user(request, _("Bookmarkings count has been reset for the selected bookmarks."))
    #
    # reset_bookmarkings_count.short_description = _("Reset bookmarkings count for selected bookmarks")

    # actions = [reset_bookmarkings_count]


admin.site.register(Bookmark, BookmarkAdmin)
