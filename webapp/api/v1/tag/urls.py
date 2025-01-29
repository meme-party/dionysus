from django.urls import path

from .views import TagListAPIView

app_name = "api.v1.tag"

urlpatterns = [
    path("", TagListAPIView.as_view(), name="tag-list"),
]
