# Generated by Django 4.2.7 on 2023-11-24 16:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("social_media", "0007_alter_userprofile_followers_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="followers",
        ),
    ]
