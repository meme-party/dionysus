from django.urls import path

from .views import FavoriteTagListAPIView, TagListAPIView

app_name = "api.v1.tag"

urlpatterns = [
    path("tags/", TagListAPIView.as_view(), name="tag-list"),
    path("favorite-tags/", FavoriteTagListAPIView.as_view(), name="favorite-tag-list"),
]
