from api.v1.meme.serializers import MemeSerializer
from django.db.models import ExpressionWrapper, F, FloatField
from django.db.models.functions import Extract, Now
from meme.models import Meme
from meme.services.increase_meme_view_count_service import IncreaseMemeViewCountService
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

POPULARITY_WEIGHTS = {
    "bookmarkings_count": 3,
    "bookmarking_users_count": 6,
    "views_count": 1,
    "viewers_count": 2,
}


class MemeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MemeSerializer
    permission_classes = [AllowAny]

    ordering_fields = ["id", "created_at", "title", "popularity"]
    search_fields = ["title", "tags__name"]
    filterset_fields = ["type", "tags__category__name"]
    ordering = ["-id"]

    def get_queryset(self):
        return (
            Meme.objects.prefetch_related("tags", "tags__category", "meme_counter")
            .published()
            .annotate(
                popularity=ExpressionWrapper(
                    -(
                        F("meme_counter__bookmarkings_count")
                        * POPULARITY_WEIGHTS["bookmarkings_count"]
                        + F("meme_counter__bookmarking_users_count")
                        * POPULARITY_WEIGHTS["bookmarking_users_count"]
                        + F("meme_counter__views_count")
                        * POPULARITY_WEIGHTS["views_count"]
                        + F("meme_counter__viewers_count")
                        * POPULARITY_WEIGHTS["viewers_count"]
                    )
                    / Extract(Now() - F("updated_at"), "epoch"),
                    output_field=FloatField(),
                )
            )
        ).order_by('id')

    def retrieve(self, request, *args, **kwargs):
        meme = self.get_object()
        IncreaseMemeViewCountService(meme, request.user).perform()

        return super().retrieve(request, *args, **kwargs)
