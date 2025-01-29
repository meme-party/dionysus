from meme.models.meme import Meme, MemeModelManager, MemeQuerySet


class AudioMeme(Meme):
    MEME_TYPE = "Audio"

    class Meta:
        proxy = True

    objects = MemeModelManager.from_queryset(MemeQuerySet)()

    def __init__(self, *args, **kwargs):
        self._meta.get_field("type").default = "Audio"
        super(AudioMeme, self).__init__(*args, **kwargs)
