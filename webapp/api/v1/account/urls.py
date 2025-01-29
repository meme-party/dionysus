from django.urls import path

app_name = "api.v1.account"

from django.http import HttpResponse


def test_view(request):
    return HttpResponse("Test view")


urlpatterns = [
    path("test/", test_view, name="test"),
]
