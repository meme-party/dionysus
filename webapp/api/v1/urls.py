from django.urls import path, include

app_name = 'api.v1'

urlpatterns = [
    path('memes/', include('api.v1.meme.urls')),
    path('users/', include('api.v1.user.urls')),
]
