from api.v1.base_api_view import BaseAPIView
from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet, BaseAPIView):
    pass
