from django.urls import path

from .views import MemeViewSet

app_name = "api.v1.meme"

urlpatterns = [
    path("", MemeViewSet.as_view({"get": "list", "post": "create"}), name="meme-list"),
    path(
        "<int:pk>/",
        MemeViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="meme-detail",
    ),
]
