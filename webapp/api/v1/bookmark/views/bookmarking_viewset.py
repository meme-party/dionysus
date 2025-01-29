from api.v1.bookmark.serializers import BookmarkingSerializer
from bookmark.models import Bookmarking
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class BookmarkingViewSet(viewsets.ModelViewSet):
    queryset = Bookmarking.objects.all()
    serializer_class = BookmarkingSerializer
    permission_classes = (
        IsAuthenticated,
    )  # TODO: 다른 유저의 bookmark는 조회할 수 없도록 수정
    search_fields = ["meme__title"]
    ordering_fields = ["created_at", "updated_at", "meme__title"]

    def get_queryset(self):
        return self.queryset.all()
