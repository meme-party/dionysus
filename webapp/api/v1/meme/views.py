from api.v1.meme.serializers import MemeSerializer
from meme.models import Meme
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.prefetch_related("tags", "tags__category").all()
    serializer_class = MemeSerializer
    permission_classes = [AllowAny]
    ordering_fields = ["created_at", "title"]
    search_fields = ["title", "tags__name"]

    # TODO(koa): 권한 설정 / 생성, 수정, 삭제는 어드민만 가능하도록 함.
