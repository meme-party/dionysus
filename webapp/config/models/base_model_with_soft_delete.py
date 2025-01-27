from django.db import models
from .base_model import BaseModel
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def with_deleted(self):
        return super().get_queryset()

    def only_deleted(self):
        return super().get_queryset().filter(deleted_at__isnull=False)


class BaseModelWithSoftDelete(BaseModel):
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    objects = SoftDeleteManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def really_delete(self):
        super().delete()

    def restore(self):
        self.deleted_at = None
        self.save()
