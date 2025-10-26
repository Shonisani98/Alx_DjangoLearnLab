from django.urls import path
from .views import like_post, unlike_post

urlpatterns = [
    path('<int:pk>/like/', like_post, name='like-post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike-post'),
]
