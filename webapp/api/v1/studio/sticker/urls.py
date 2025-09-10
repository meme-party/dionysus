from api.v1.studio.sticker.views.sticker_viewset import StickerViewSet
from django.urls import include, path
from rest_framework_nested.routers import DefaultRouter

app_name = "api.v1.studio.sticker"

router = DefaultRouter()
router.register(r"stickers", StickerViewSet, basename="sticker")

urlpatterns = [
    path("", include(router.urls)),
]
