from bookmark.models import Bookmarking
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


@receiver(post_save, sender=Bookmarking)
def update_bookmarkings_count_on_save(sender, instance, created, **kwargs):
    instance.bookmark.reset_bookmarkings_count()


@receiver(post_delete, sender=Bookmarking)
def update_bookmarkings_count_on_delete(sender, instance, **kwargs):
    instance.bookmark.reset_bookmarkings_count()
