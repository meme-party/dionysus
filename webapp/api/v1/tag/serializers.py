from rest_framework import serializers
from tag.models import Tag, TagCategory


class TagCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TagCategory
        fields = ["id", "name"]


class TagSerializer(serializers.ModelSerializer):
    category = TagCategorySerializer()

    class Meta:
        model = Tag
        fields = ["id", "name", "category"]
