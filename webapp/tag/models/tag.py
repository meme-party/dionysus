from config.models import BaseModelWithSoftDelete, SoftDeleteManager
from django.db import models
from django.db.models import QuerySet


class TagQuerySet(QuerySet):
    def preparing(self):
        return self.active().filter(published_at__isnull=True)

    def published(self):
        return self.active().filter(published_at__isnull=False)

    def active(self):
        return self.filter(archived_at__isnull=True)

    def archived(self):
        return self.filter(archived_at__isnull=False)


class Tag(BaseModelWithSoftDelete):
    class Meta:
        db_table = "tags"
        verbose_name = "tag"
        verbose_name_plural = "tags"

    objects = SoftDeleteManager.from_queryset(TagQuerySet)()

    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)

    category = models.ForeignKey(
        "tag.TagCategory",
        on_delete=models.CASCADE,
        related_name="tags",
    )

    memes = models.ManyToManyField(
        "meme.Meme",
        through="tag.MemeTagging",
        related_name="tag",
    )

    published_at = models.DateTimeField(
        verbose_name="published at",
        null=True,
        blank=True,
    )

    archived_at = models.DateTimeField(
        verbose_name="archived at",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
