from api.v1.bookmark.views import BookmarkingViewSet, BookmarkViewSet
from django.urls import include, path
from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter

app_name = "api.v1.bookmark"

router = DefaultRouter()
router.register(r"bookmarks", BookmarkViewSet, basename="bookmark")

bookmarking_router = NestedSimpleRouter(router, r"bookmarks", lookup="bookmark")
bookmarking_router.register(r"bookmarkings", BookmarkingViewSet, basename="bookmarking")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(bookmarking_router.urls)),
]
