from django.urls import path, include
from social_media.views import ProfileViewSet, PostViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("profiles", ProfileViewSet, basename="profiles")
router.register("posts", PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "social_media"
