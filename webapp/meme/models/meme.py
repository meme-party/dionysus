from config.models import BaseModelWithSoftDelete, SoftDeleteManager
from django.conf import settings
from django.db import models
from django.db.models import QuerySet

TYPE_CHOICES = (
    ("Text", "Text"),
    ("Image", "Image"),
    ("Video", "Video"),
    ("Audio", "Audio"),
)


class MemeModelManager(SoftDeleteManager):
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.MEME_TYPE)


class MemeQuerySet(QuerySet):
    def preparing(self):
        return self.active().filter(published_at__isnull=True)

    def published(self):
        return self.active().filter(published_at__isnull=False)

    def active(self):
        return self.filter(archived_at__isnull=True)

    def archived(self):
        return self.filter(archived_at__isnull=False)


class Meme(BaseModelWithSoftDelete):
    MEME_TYPE = ""

    class Meta:
        db_table = "memes"
        verbose_name = "meme"
        verbose_name_plural = "memes"

        indexes = [
            models.Index(fields=["type"]),
        ]

    type = models.CharField(
        verbose_name="meme type",
        max_length=10,
        blank=False,
        null=False,
        choices=TYPE_CHOICES,
    )

    title = models.CharField(
        verbose_name="meme title", max_length=100, blank=False, null=False
    )

    # TODO(koa): title 컬럼에 대하여 GIN Index 도입
    # 데이터 및 쿼리에 따라 Full Text Search 확인 후 GIN Index 도입 여부 결정하기

    description = models.TextField(
        verbose_name="meme description", blank=False, null=False
    )

    original_link = models.TextField(
        verbose_name="original link",
        max_length=100,
        blank=True,
        null=True,
    )

    published_at = models.DateTimeField(
        verbose_name="published at",
        blank=True,
        null=True,
    )

    archived_at = models.DateTimeField(
        verbose_name="archived at",
        blank=True,
        null=True,
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="creator",
        related_name="created_memes",
        on_delete=models.CASCADE,
    )

    tags = models.ManyToManyField(
        "tag.Tag",
        through="tag.MemeTagging",
        related_name="meme",
    )

    thumbnail = models.ForeignKey(
        "file_manager.Thumbnail",
        verbose_name="thumbnail",
        related_name="meme",
        on_delete=models.SET_NULL,
        null=True,
    )
