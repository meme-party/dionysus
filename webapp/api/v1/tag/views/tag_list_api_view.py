from api.v1.tag.serializers import TagSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from tag.models import Tag


# TODO(koa): 인기도에 따라 태그를 정렬하는 API를 구현해야함.
# TODO(koa): 태그 관련하여 자동완성 기능을 구현해야함.
class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["category", "first_letter"]
    search_fields = ["name", "split_name"]

    def get_queryset(self):
        return self.queryset.all()
