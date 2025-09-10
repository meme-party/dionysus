from config.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserSticker(BaseModel):
    """사용자가 보유한(구매한) 스티커 모델"""

    class Meta:
        db_table = "studio_user_stickers"
        verbose_name = "User Sticker"
        verbose_name_plural = "User Stickers"
        unique_together = ("user", "sticker")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sticker = models.ForeignKey("Sticker", on_delete=models.CASCADE)
