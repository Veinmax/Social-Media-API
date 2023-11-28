from rest_framework import serializers
from social_media.models import Profile, Post


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "id",
            "username",
            "gender",
            "bio",
            "lives_in",
            "phone",
            "created_at",
            "profile_picture",
            "following",
        )


class ProfileListSerializer(ProfileSerializer):
    class Meta:
        model = Profile
        fields = (
            "id",
            "username",
            "gender",
            "bio",
            "profile_picture",
        )


class ProfileDetailSerializer(ProfileSerializer):
    class Meta:
        model = Profile
        fields = (
            "id",
            "username",
            "gender",
            "bio",
            "lives_in",
            "phone",
            "created_at",
            "profile_picture",
            "following",
            "followers",
        )
        read_only_fields = (
            "id",
            "followers",
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "content", "post_picture", "category")
