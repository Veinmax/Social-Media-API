from rest_framework import serializers
from social_media.models import Profile, Post, Comment, Like


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


class CommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.ReadOnlyField(source="owner.profile.username")

    class Meta:
        model = Comment
        fields = ("id", "content", "comment_date", "commented_by", "post")


class LikeSerializer(serializers.ModelSerializer):
    like = serializers.ReadOnlyField(source="like.profile.username")

    class Meta:
        model = Like
        fields = ("id", "post", "like")


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "content", "post_picture", "category", "comments", "likes")
