from django.urls import include, path

app_name = "api.v1"

urlpatterns = [
    path("memes/", include("api.v1.meme.urls")),
    path("users/", include("api.v1.account.urls")),
    path("tags/", include("api.v1.tag.urls")),
    path("", include("api.v1.bookmark.urls")),
]
