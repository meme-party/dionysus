from config.models import BaseModel
from django.db import models


class Bookmarking(BaseModel):
    class Meta:
        db_table = "bookmarkings"
        verbose_name = "bookmarking"
        verbose_name_plural = "bookmarkings"
        indexes = [
            models.Index(fields=["meme", "bookmark"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["meme", "bookmark"],
                name="unique_meme_bookmark",
            )
        ]

    bookmark = models.ForeignKey(
        "bookmark.Bookmark",
        verbose_name="bookmark",
        related_name="bookmarkings",
        on_delete=models.CASCADE,
    )

    meme = models.ForeignKey(
        "meme.Meme",
        verbose_name="meme",
        related_name="bookmarkings",
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        "account.User",
        verbose_name="user",
        related_name="bookmarkings",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.bookmark} - {self.meme}"

    def save(self, *args, **kwargs):
        self.user = self.bookmark.user
        super().save(*args, **kwargs)
