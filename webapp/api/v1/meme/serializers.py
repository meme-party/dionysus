from api.v1.file_manager.serializers import ThumbnailSerializer
from api.v1.tag.serializers import TagSerializer
from file_manager.models import Thumbnail
from meme.models import Meme
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from tag.models import Tag


class MemeSerializer(serializers.ModelSerializer):
    tag_ids = PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        write_only=True,
    )
    thumbnail_id = PrimaryKeyRelatedField(
        queryset=Thumbnail.objects.all(),
        write_only=True,
    )

    tags = TagSerializer(many=True, read_only=True)
    thumbnail = ThumbnailSerializer(read_only=True)

    class Meta:
        model = Meme
        fields = [
            "id",
            "title",
            "type",
            "description",
            "thumbnail_id",
            "thumbnail",
            "original_link",
            "tag_ids",
            "tags",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "tags",
            "thumbnail",
            "created_at",
            "updated_at",
        ]
