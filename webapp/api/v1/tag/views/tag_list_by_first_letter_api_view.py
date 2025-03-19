from collections import defaultdict

from api.v1.tag.serializers import TagSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from tag.models import Tag


class TagListByFirstLetterAPIView(APIView):
    permission_classes = (AllowAny,)

    """
    각 태그의 first_letter를 기준으로 그룹핑하여, 각 태그마다 요소별로 최대 5개씩만 가져오는 API View
    """

    @staticmethod
    def get(request):
        count = int(request.GET.get("count", 5))
        order_by = request.GET.get("order_by", "name")

        tags = Tag.objects.all().order_by("first_letter", order_by)
        tags_by_first_letter = defaultdict(list)
        for tag in tags:
            tags_by_first_letter[tag.first_letter].append(tag)

        tags_by_first_letter = dict(tags_by_first_letter)
        for key in tags_by_first_letter.keys():
            tags_by_first_letter[key] = sorted(
                tags_by_first_letter[key], key=lambda x: getattr(x, order_by)
            )
            tags_by_first_letter[key] = tags_by_first_letter[key][:count]
            tags_by_first_letter[key] = TagSerializer(
                tags_by_first_letter[key], many=True
            ).data

        return Response(tags_by_first_letter)
