from api.v1.tag.serializers import TagSerializer
from meme.models import Meme
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from tag.models import Tag


class MemeSerializer(serializers.ModelSerializer):
    tag_ids = PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        write_only=True,
    )
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Meme
        fields = [
            "id",
            "title",
            "type",
            "description",
            "thumbnail",
            "original_link",
            "tag_ids",
            "tags",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "created_at",
            "updated_at",
        ]
