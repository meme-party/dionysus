from meme.models.meme import Meme, MemeModelManager, MemeQuerySet


class VideoMeme(Meme):
    MEME_TYPE = "Video"

    class Meta:
        proxy = True

    objects = MemeModelManager.from_queryset(MemeQuerySet)()

    def __init__(self, *args, **kwargs):
        self._meta.get_field("type").default = "Video"
        super(VideoMeme, self).__init__(*args, **kwargs)
