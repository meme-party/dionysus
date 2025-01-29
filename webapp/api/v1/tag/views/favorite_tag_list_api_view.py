from account.models import UserTagCounter
from api.v1.tag.serializers import TagSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from tag.models import Tag


class FavoriteTagListAPIView(ListAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tags = (
            UserTagCounter.objects.prefetch_related("tag")
            .filter(user=self.request.user)
            .order_by("-bookmarkings_count")
            .values_list("tag", flat=True)[:10]
        )

        return Tag.objects.filter(id__in=tags)
