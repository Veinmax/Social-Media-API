from django.urls import path, include
from social_media.views import ProfileViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("profiles", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "social_media"
