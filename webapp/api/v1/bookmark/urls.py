from api.v1.bookmark.views import (
    BookmarkingDeleteAPIView,
    BookmarkingSyncAPIView,
    BookmarkingViewSet,
    BookmarkViewSet,
)
from django.urls import include, path
from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter

app_name = "bookmark"

router = DefaultRouter()
router.register(r"bookmarks", BookmarkViewSet, basename="bookmark")

bookmarking_router = NestedSimpleRouter(router, r"bookmarks", lookup="bookmark")
bookmarking_router.register(r"bookmarkings", BookmarkingViewSet, basename="bookmarking")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(bookmarking_router.urls)),
    path("bookmarkings/", BookmarkingSyncAPIView.as_view(), name="bookmarking-sync"),
    path(
        "bookmarkings/<int:bookmarking_id>",
        BookmarkingDeleteAPIView.as_view(),
        name="bookmarking-delete",
    ),
]
