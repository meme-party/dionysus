from file_manager.models import Thumbnail
from rest_framework.serializers import ModelSerializer


class ThumbnailSerializer(ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["url"]
