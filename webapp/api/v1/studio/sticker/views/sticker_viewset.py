from api.shared.pagination.standard_page_pagination import StandardPagePagination
from api.v1.base_viewset import BaseViewSet
from api.v1.studio.sticker.permissions.sticker_permission import StickerPermission
from api.v1.studio.sticker.serializers.sticker_serializer import StickerSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import filters
from studio.models import Sticker


@extend_schema(
    tags=["studio"],
    summary="스티커 API",
    description="스티커 목록을 조회하거나 생성, 수정, 삭제합니다.",
)
class StickerViewSet(BaseViewSet):
    serializer_class = StickerSerializer
    permission_classes = [StickerPermission]
    pagination_class = StandardPagePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]
    lookup_field = "id"

    def get_queryset(self):
        return Sticker.objects.usable_by(self.current_user)

    def perform_create(self, serializer):
        serializer.save(creator=self.current_user)
