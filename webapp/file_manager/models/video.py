from config.models import BaseModelWithSoftDelete
from django.db import models


class Video(BaseModelWithSoftDelete):
    class Meta:
        db_table = "videos"
        verbose_name = "video"
        verbose_name_plural = "videos"

    name = models.CharField(
        max_length=255,
        verbose_name="이름",
        null=False,
        blank=False,
        default="video",
    )

    file = models.FileField(
        upload_to="videos/",
        verbose_name="파일",
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    @property
    def url(self):
        return self.file.url
