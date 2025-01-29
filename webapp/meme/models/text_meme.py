from meme.models.meme import Meme, MemeModelManager, MemeQuerySet


class TextMeme(Meme):
    MEME_TYPE = "Text"

    class Meta:
        proxy = True

    objects = MemeModelManager.from_queryset(MemeQuerySet)()

    def __init__(self, *args, **kwargs):
        self._meta.get_field("type").default = "Text"
        super(TextMeme, self).__init__(*args, **kwargs)
