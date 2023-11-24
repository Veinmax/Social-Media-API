from django.urls import path, include
from social_media.views import UserProfileViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("profiles", UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "social_media"
