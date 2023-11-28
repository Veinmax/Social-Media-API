from django.urls import path, include
from social_media.views import ProfileViewSet, PostViewSet, CommentViewSet, LikeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)
router.register("likes", LikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "social_media"
