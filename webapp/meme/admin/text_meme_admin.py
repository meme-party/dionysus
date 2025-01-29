from django.contrib import admin
from meme.models import TextMeme

from .meme_admin import MemeAdmin


@admin.register(TextMeme)
class TextMemeAdmin(MemeAdmin):
    pass
