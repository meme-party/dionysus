from django.urls import include, path

app_name = "api.v1.studio"

urlpatterns = [
    path("studio/", include("api.v1.studio.sticker.urls")),
]
