from django.contrib import admin
from meme.models import AudioMeme

from .meme_admin import MemeAdmin


@admin.register(AudioMeme)
class AudioMemeAdmin(MemeAdmin):
    pass
