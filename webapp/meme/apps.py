from django.apps import AppConfig


class MemeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "meme"

    def ready(self):
        import meme.signals

        return super().ready()
