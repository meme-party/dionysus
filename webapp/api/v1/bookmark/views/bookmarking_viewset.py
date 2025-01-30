from api.v1.bookmark.serializers import BookmarkingSerializer
from bookmark.models import Bookmark, Bookmarking
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class BookmarkingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bookmarking.objects.all()
    serializer_class = BookmarkingSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ["meme__title"]
    ordering_fields = ["created_at", "updated_at", "meme__title"]

    def get_queryset(self):
        bookmark_pk = self.kwargs.get("bookmark_pk")
        bookmark = get_object_or_404(Bookmark, pk=bookmark_pk, user=self.request.user)

        return self.queryset.filter(user=self.request.user, bookmark=bookmark)
