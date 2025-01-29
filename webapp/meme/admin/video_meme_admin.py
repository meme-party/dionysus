from django.contrib import admin
from meme.models import VideoMeme

from .meme_admin import MemeAdmin


@admin.register(VideoMeme)
class VideoMemeAdmin(MemeAdmin):
    pass
