from django.urls import path

from .views import KakaoLogin, kakao_callback, kakao_login

app_name = "api.v1.account"


urlpatterns = [
    path("accounts/kakao/login/", kakao_login, name="kakao_login"),
    path("accounts/kakao/login/callback/", kakao_callback, name="kakao_callback"),
    path(
        "accounts/kakao/login/finish/",
        KakaoLogin.as_view(),
        name="kakao_login_todjango",
    ),
]
