from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from social_media.permissions import IsOwnerOrIfAuthenticatedReadOnly

from social_media.models import UserProfile
from social_media.serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsOwnerOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        """Retrieve the movies with filters"""
        username = self.request.query_params.get("username")

        queryset = self.queryset

        if username:
            queryset = queryset.filter(username__icontains=username)

        return queryset.distinct()

    def perform_create(self, serializer):
        if UserProfile.objects.filter(owner=self.request.user).exists():
            raise ValidationError("You already have a profile.")
        serializer.save(owner=self.request.user)
