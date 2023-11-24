import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify


def profile_custom_path(instance, filename):
    _, extension = os.path.splitext(filename)
    return os.path.join(
        "uploads",
        "profile_images",
        f"{slugify(instance.username)}-{uuid.uuid4()}{extension}",
    )


class UserProfile(models.Model):
    class GenderChoices(models.Choices):
        MALE = "Male"
        FEMALE = "Female"

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile_data"
    )
    username = models.CharField(max_length=60)
    grade = models.CharField(max_length=10, choices=GenderChoices.choices)
    bio = models.TextField()
    lives_in = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(
        null=True, blank=True, upload_to=profile_custom_path
    )

    def __str__(self):
        return f"Profile of {self.username}"
