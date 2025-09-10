from config.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models, transaction

User = get_user_model()


class UserTicketHistory(BaseModel):
    """사용자의 티켓 변동 이력 모델"""

    class Meta:
        db_table = "studio_user_ticket_histories"
        verbose_name = "User Ticket History"
        verbose_name_plural = "User Ticket Histories"

    ACTION_CHOICES = [
        ("purchase", "Purchase"),
        ("buy_sticker", "Buy Sticker"),
        ("use_template", "Use Template"),
        ("earn_from_sticker_share", "Earn from Sticker Share"),
        ("earn_from_template_share", "Earn from Template Share"),
        ("admin_adjustment", "Admin Adjustment"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=30, choices=ACTION_CHOICES)
    amount = models.IntegerField()  # 변동된 티켓 수량
    description = models.TextField(blank=True, null=True)  # 변동 사유 등 추가 정보
    sticker = models.ForeignKey(
        "Sticker", on_delete=models.SET_NULL, null=True, blank=True
    )
    canvas = models.ForeignKey(
        "Canvas", on_delete=models.SET_NULL, null=True, blank=True
    )

    @classmethod
    @transaction.atomic
    def record_history(
        cls, user, action, amount, description="", sticker=None, canvas=None
    ):
        cls.objects.create(
            user=user,
            action=action,
            amount=amount,
            description=description,
            sticker=sticker,
            canvas=canvas,
        )

        ticket = user.user_ticket
        ticket.amount += amount

        if ticket.amount < 0:
            raise ValueError("Not enough tickets")

        ticket.save()
