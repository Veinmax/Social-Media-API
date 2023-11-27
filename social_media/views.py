from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from social_media.permissions import IsOwnerOrIfAuthenticatedReadOnly

from social_media.models import Profile
from social_media.serializers import (
    ProfileSerializer,
    ProfileDetailSerializer,
    ProfileListSerializer,
)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        username = self.request.query_params.get("username")

        queryset = self.queryset

        if username:
            queryset = queryset.filter(username__icontains=username)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return ProfileListSerializer

        if self.action == "retrieve":
            return ProfileDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        if Profile.objects.filter(owner=self.request.user).exists():
            raise ValidationError("You already have a profile.")
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["get"])
    def follow(self, request, pk=None):
        profile_to_follow = self.get_object()

        if profile_to_follow == self.request.user.profile:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.request.user.profile.following.add(profile_to_follow)
        return Response(
            {"detail": "You are now following this user"}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["get"])
    def unfollow(self, request, pk=None):
        profile_to_unfollow = self.get_object()
        self.request.user.profile.following.remove(profile_to_unfollow)
        return Response(
            {"detail": "You are now unfollowing this user"}, status=status.HTTP_200_OK
        )
