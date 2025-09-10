from rest_framework import serializers
from studio.models import Sticker


class StickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticker
        fields = ["id", "name", "image", "description", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
