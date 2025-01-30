from config.models import BaseModelWithSoftDelete
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q


class MemeTagging(BaseModelWithSoftDelete):
    class Meta:
        db_table = "meme_taggings"
        verbose_name = "meme_tagging"
        verbose_name_plural = "meme_taggings"
        indexes = [models.Index(fields=["meme", "tag"])]
        constraints = [
            models.UniqueConstraint(
                fields=["meme", "tag"],
                name="unique_meme_tag",
                condition=Q(deleted_at__isnull=True),
            )
        ]

    meme = models.ForeignKey(
        "meme.Meme",
        on_delete=models.CASCADE,
        related_name="meme_taggings",
    )

    tag = models.ForeignKey(
        "tag.Tag",
        on_delete=models.CASCADE,
        related_name="meme_taggings",
    )

    def clean(self):
        super().clean()

        if self.deleted_at is None:
            pre_existing_meme_taggings = MemeTagging.objects.filter(meme=self.meme)
            if self.pk:
                pre_existing_meme_taggings = pre_existing_meme_taggings.exclude(
                    pk=self.pk
                )

            pre_existing_meme_taggings_count = pre_existing_meme_taggings.count()
            if pre_existing_meme_taggings_count >= 10:
                raise ValidationError({"tag": "A Meme cannot have more than 10 tags."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.meme} - {self.tag}"
