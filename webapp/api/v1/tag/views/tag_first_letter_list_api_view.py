from rest_framework.response import Response
from rest_framework.views import APIView
from tag.models import Tag


class TagFirstLetterListAPIView(APIView):

    @staticmethod
    def get(request):
        first_letters = Tag.objects.values_list("first_letter", flat=True).distinct()

        return Response(first_letters)
