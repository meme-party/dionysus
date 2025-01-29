from file_manager.models import Audio
from rest_framework.serializers import ModelSerializer


class AudioSerializer(ModelSerializer):
    class Meta:
        model = Audio
        fields = ["url"]
