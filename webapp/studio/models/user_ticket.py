from config.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserTicket(BaseModel):
    """사용자가 보유한 티켓 모델"""

    class Meta:
        db_table = "studio_user_tickets"
        verbose_name = "User Ticket"
        verbose_name_plural = "User Tickets"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, unique=True, related_name="user_ticket"
    )
    amount = models.IntegerField(default=0)  # 티켓 수량
