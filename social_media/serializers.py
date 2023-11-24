from rest_framework import serializers
from social_media.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    # followers = serializers.SlugRelatedField()

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "username",
            "grade",
            "bio",
            "lives_in",
            "phone",
            "created_at",
            "profile_picture",
            "followers",
            "following",
        )
        read_only_fields = ("followers",)
