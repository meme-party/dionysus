from api.v1.meme.serializers import MemeSerializer
from meme.models import Meme
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class MemeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Meme.objects.prefetch_related("tags", "tags__category").published()

    serializer_class = MemeSerializer
    permission_classes = [AllowAny]

    ordering_fields = ["created_at", "title"]
    search_fields = ["title", "tags__name"]
    filterset_fields = ["type", "tags__category__name"]
