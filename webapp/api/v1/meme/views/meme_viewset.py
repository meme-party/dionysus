from api.v1.meme.serializers import MemeSerializer
from meme.models import Meme
from meme.services.increase_meme_view_count_service import IncreaseMemeViewCountService
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class MemeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Meme.objects.prefetch_related("tags", "tags__category").published()

    serializer_class = MemeSerializer
    permission_classes = [AllowAny]

    ordering_fields = ["created_at", "title"]
    search_fields = ["title", "tags__name"]
    filterset_fields = ["type", "tags__category__name"]

    def retrieve(self, request, *args, **kwargs):
        meme = self.get_object()
        IncreaseMemeViewCountService(meme, request.user).perform()

        return super().retrieve(request, *args, **kwargs)
