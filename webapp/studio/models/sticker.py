from config.models import BaseModel, BaseModelManager, BaseModelQuerySet
from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.db.models import Q
from django.utils import timezone
from studio.models.user_sticker import UserSticker
from studio.models.user_ticket_history import UserTicketHistory

User = get_user_model()


class StickerQuerySet(BaseModelQuerySet):
    def active(self):
        # 사용자는 무조건 active 상태의 스티커만 볼 수 있어야 함
        return self.filter(active_at__isnull=False, inactive_at__isnull=True)

    def inactive(self):
        return self.filter(active_at__isnull=True, inactive_at__isnull=False)

    def free(self):
        return self.filter(ticket_price=0)

    def usable_by(self, user):
        stickers = self.active()

        if user.is_anonymous:
            return stickers.none()

        user_stickers = UserSticker.objects.filter(user=user)
        return stickers.filter(
            Q(ticket_price=0)
            | Q(id__in=user_stickers.values_list("sticker_id", flat=True))
        )

    def bulk_activate(self):
        self.update(active_at=timezone.now(), inactive_at=None)
        return self

    def bulk_inactivate(self):
        self.update(active_at=None, inactive_at=timezone.now())
        return self


class StickerManager(BaseModelManager.from_queryset(StickerQuerySet)):
    pass


class Sticker(BaseModel):
    class Meta:
        db_table = "studio_stickers"
        verbose_name = "Sticker"
        verbose_name_plural = "Stickers"

    objects = StickerManager()

    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="stickers/")
    description = models.TextField(blank=True, null=True)
    active_at = models.DateTimeField(blank=True, null=True)
    inactive_at = models.DateTimeField(blank=True, null=True)
    ticket_price = models.IntegerField(default=0)  # 티켓 단위 가격으로 처리
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def active(self):
        return self.active_at is not None and self.inactive_at is None

    def use(self, user):
        """스티커 사용
        이미 구매한 스티커라면 사용하고, 구매하지 않은 스티커라면 구매한 후 사용하도록 처리함
        """
        user_sticker = UserSticker.objects.filter(user=user, sticker=self).first()
        if not user_sticker:
            user_sticker = self.buy(user)

        return user_sticker

    @transaction.atomic
    def buy(self, user):
        """스티커 구매
        UserTicketHistory를 통해 구매 이력 기록 및 Ticket 처리 수행
        """
        user_sticker, created = UserSticker.objects.get_or_create(
            user=user, sticker=self
        )
        if not created:
            raise ValueError("Already bought this sticker")

        UserTicketHistory.record_history(
            user=user, sticker=self, amount=-self.ticket_price, action="buy_sticker"
        )

        return user_sticker

    def activate(self):
        self.active_at = timezone.now()
        self.inactive_at = None
        self.save()

    def inactivate(self):
        self.active_at = None
        self.inactive_at = timezone.now()
        self.save()
