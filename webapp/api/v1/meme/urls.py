from api.v1.meme.views import MemeViewSet
from django.urls import include, path
from rest_framework_nested.routers import DefaultRouter

app_name = "api.v1.meme"

router = DefaultRouter()
router.register(r"memes", MemeViewSet, basename="meme")

urlpatterns = [
    path("", include(router.urls)),
]
