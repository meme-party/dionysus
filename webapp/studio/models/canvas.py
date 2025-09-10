from config.models import BaseModel, BaseModelManager, BaseModelQuerySet
from django.contrib.auth import get_user_model
from django.db import models

from .sticker import Sticker

User = get_user_model()


class CanvasQuerySet(BaseModelQuerySet):
    def public(self):
        return self.filter(is_public=True)

    def templates(self):
        return self.filter(is_template=True)

    def by_owner(self, user):
        return self.filter(owner=user)

    def accessible_by(self, user):
        if user.is_authenticated:
            return self.filter(models.Q(is_public=True) | models.Q(owner=user))
        return self.is_public()

    def templates_accessible_by(self, user):
        self.templates().accessible_by(user)


class CanvasManager(BaseModelManager.from_queryset(CanvasQuerySet)):
    pass


class Canvas(BaseModel):
    class Meta:
        db_table = "studio_canvases"
        verbose_name = "Canvas"
        verbose_name_plural = "Canvases"

    objects = CanvasManager()

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    background_color = models.CharField(max_length=7, default="#FFFFFF")
    content = models.JSONField(default=list)
    is_public = models.BooleanField(default=False)
    is_template = models.BooleanField(default=False)
    using_stickers = models.ManyToManyField(Sticker, related_name="canvases")

    preview_image = models.ImageField(
        upload_to="canvas_previews/", blank=True, null=True
    )
    complete_image = models.ImageField(
        upload_to="canvas_completes/", blank=True, null=True
    )
