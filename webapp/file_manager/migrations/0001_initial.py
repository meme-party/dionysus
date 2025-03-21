# Generated by Django 5.1.5 on 2025-03-16 07:46

import config.models.base_model_with_soft_delete
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Audio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "name",
                    models.CharField(
                        default="audio", max_length=255, verbose_name="이름"
                    ),
                ),
                ("file", models.FileField(upload_to="audios/", verbose_name="파일")),
            ],
            options={
                "verbose_name": "audio",
                "verbose_name_plural": "audios",
                "db_table": "audios",
            },
            managers=[
                (
                    "objects",
                    config.models.base_model_with_soft_delete.SoftDeleteManager(),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Thumbnail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "name",
                    models.CharField(
                        default="thumbnail", max_length=255, verbose_name="이름"
                    ),
                ),
                (
                    "file",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="thumbnails/",
                        verbose_name="썸네일 파일",
                    ),
                ),
                (
                    "web_url",
                    models.URLField(
                        blank=True,
                        help_text="웹에서 접근할 수 있는 URL, 파일이 없는 경우 사용됩니다.",
                        null=True,
                        verbose_name="웹 URL",
                    ),
                ),
            ],
            options={
                "verbose_name": "thumbnail",
                "verbose_name_plural": "thumbnails",
                "db_table": "thumbnails",
            },
            managers=[
                (
                    "objects",
                    config.models.base_model_with_soft_delete.SoftDeleteManager(),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "name",
                    models.CharField(
                        default="video", max_length=255, verbose_name="이름"
                    ),
                ),
                ("file", models.FileField(upload_to="videos/", verbose_name="파일")),
            ],
            options={
                "verbose_name": "video",
                "verbose_name_plural": "videos",
                "db_table": "videos",
            },
            managers=[
                (
                    "objects",
                    config.models.base_model_with_soft_delete.SoftDeleteManager(),
                ),
            ],
        ),
    ]
