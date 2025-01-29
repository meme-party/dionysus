from file_manager.models import Video
from rest_framework.serializers import ModelSerializer


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ["url"]
