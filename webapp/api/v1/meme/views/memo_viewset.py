from api.v1.meme.serializers import MemoSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


@extend_schema_view(
    list=extend_schema(
        tags=["meme-memo"],
    ),
    retrieve=extend_schema(
        tags=["meme-memo"],
    ),
    create=extend_schema(
        tags=["meme-memo"],
    ),
    update=extend_schema(
        tags=["meme-memo"],
    ),
    partial_update=extend_schema(
        tags=["meme-memo"],
    ),
    destroy=extend_schema(
        tags=["meme-memo"],
    ),
)
class MemoViewSet(viewsets.ModelViewSet):
    serializer_class = MemoSerializer
    permission_classes = [IsAuthenticated]

    ordering_fields = ["id", "created_at", "updated_at"]
    search_fields = []
    filterset_fields = []
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        return self.request.user.memos.all()
