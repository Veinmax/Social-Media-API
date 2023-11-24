from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
        # if UserProfile.objects.filter(owner=self.request.user).exists():
        #     raise ValidationError("You already have a profile.")
        # serializer.save(owner=self.request.user)
        user = self.request.user
        profile, created = UserProfile.objects.get_or_create(user)
        if created:
            profile.save()
        serializer.instance = profile

    @action(methods=["POST"], detail=True)
    def follow(self, request, pk=None):
        # user = request.user
        # profile = UserProfile.objects.get(pk=pk)
        profile = self.get_object()
        user_to_follow = get_object_or_404(settings.AUTH_USER_MODEL, pk=pk)
        print(user_to_follow, self.request.user)
        if self.request.user != user_to_follow:
            profile.followers.add(user_to_follow)
            return Response("You are follow", status=status.HTTP_200_OK)
        return Response(
            "You cannot follow your self", status=status.HTTP_400_BAD_REQUEST
        )

        # if profile.owner != user:
        #     if not user.following.filter(pk=pk).exists():
        #         user.following.add(pk)
        #
        #         return Response({"message": "You have followed this user."})
        #
        #     return Response({"message": "You are already following this user."})
        #
        # return Response({"message": "You cannot follow yourself."})

    @action(methods=["POST"], detail=True)
    def unfollow(self, request, pk=None):
        user = request.user
        profile = UserProfile.objects.get(pk=pk)

        if profile.owner != user:
            if user.following.filter(pk=pk).exists():
                user.following.remove(pk)
                profile.followers.remove(user)
                return Response({"message": "You have unfollowed this user."})
            else:
                return Response({"message": "You are not following this user."})
        else:
            return Response({"message": "You cannot unfollow yourself."})
