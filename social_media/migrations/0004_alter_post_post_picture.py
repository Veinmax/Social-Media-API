# Generated by Django 4.2.7 on 2023-11-27 20:55

from django.db import migrations, models
import social_media.models


class Migration(migrations.Migration):
    dependencies = [
        ("social_media", "0003_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to=social_media.models.post_custom_path
            ),
        ),
    ]
