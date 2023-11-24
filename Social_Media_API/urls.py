from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("user.urls", namespace="user")),
    path("api/social/", include("social_media.urls", namespace="social_media")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
