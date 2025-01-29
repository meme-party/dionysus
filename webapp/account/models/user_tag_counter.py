from config.models import BaseModel
from config.models.base_model import BaseModelManager
from config.settings.base import AUTH_USER_MODEL
from django.db import models
from django.db.models import Count, Q
from tag.models import Tag


class UserTagCounter(BaseModel):
    class Meta:
        db_table = "user_tag_counters"
        verbose_name = "user_tag_counter"
        verbose_name_plural = "user_tag_counters"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "tag"], name="unique_user_tag_counter"
            )
        ]

    objects = BaseModelManager()

    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tag_counters"
    )
    tag = models.ForeignKey(
        "tag.Tag", on_delete=models.CASCADE, related_name="tag_counters"
    )
    bookmarks_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    bookmarkings_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # TODO: views_count?

    def __str__(self):
        return f"{self.user.email} - {self.tag.name} - {self.count}"

    @classmethod
    def reset_all_counters(cls, user):
        tag_counts_qs = Tag.objects.filter(
            meme__bookmarkings__bookmark__user=user
        ).annotate(
            bc=Count(
                "meme__bookmarkings", filter=Q(meme__bookmarkings__bookmark__user=user)
            ),
            bkc=Count("meme__bookmarkings__bookmark", distinct=True),
        )

        rows = []
        for tag in tag_counts_qs:
            rows.append(
                {
                    "user_id": user.pk,
                    "tag_id": tag.pk,
                    "bookmarkings_count": tag.bc,
                    "bookmarks_count": tag.bkc,
                }
            )

        cls.objects.bulk_upsert(
            conflict_target=["user", "tag"],
            rows=rows,
            return_model=False,
        )
