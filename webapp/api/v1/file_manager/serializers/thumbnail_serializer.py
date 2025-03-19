from file_manager.models import Thumbnail
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class ThumbnailSerializer(ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["url"]

    url = serializers.SerializerMethodField("get_url")

    def get_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.url)
