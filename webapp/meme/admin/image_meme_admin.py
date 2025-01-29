from django.contrib import admin
from meme.models import ImageMeme

from .meme_admin import MemeAdmin


@admin.register(ImageMeme)
class ImageMemeAdmin(MemeAdmin):
    pass
