from django.db.models.signals import post_save
from django.dispatch import receiver
from meme.models import Meme, MemeCounter


@receiver(post_save, sender=Meme)
def create_meme_counter(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, "meme_counter"):
            MemeCounter.objects.create(meme=instance)
