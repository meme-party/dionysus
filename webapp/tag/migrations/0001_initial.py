# Generated by Django 5.1.5 on 2025-03-16 07:46

import config.models.base_model_with_soft_delete
import django.db.models.deletion
import tag.models.tag
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("meme", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TagCategory",
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "tag_category",
                "verbose_name_plural": "tag_categories",
                "db_table": "tag_categories",
            },
            managers=[
                (
                    "objects",
                    config.models.base_model_with_soft_delete.SoftDeleteManager(),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MemeTagging",
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
                    "meme",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meme_taggings",
                        to="meme.meme",
                    ),
                ),
            ],
            options={
                "verbose_name": "meme_tagging",
                "verbose_name_plural": "meme_taggings",
                "db_table": "meme_taggings",
            },
            managers=[
                (
                    "objects",
                    config.models.base_model_with_soft_delete.SoftDeleteManager(),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("split_name", models.CharField(default="", max_length=1000)),
                (
                    "first_letter",
                    models.CharField(db_index=True, default="", max_length=1),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "published_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="published at"
                    ),
                ),
                (
                    "archived_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="archived at"
                    ),
                ),
                (
                    "memes",
                    models.ManyToManyField(
                        related_name="tag", through="tag.MemeTagging", to="meme.meme"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags",
                        to="tag.tagcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "tag",
                "verbose_name_plural": "tags",
                "db_table": "tags",
            },
            managers=[
                ("objects", tag.models.tag.TagModelManager()),
            ],
        ),
        migrations.AddField(
            model_name="memetagging",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="meme_taggings",
                to="tag.tag",
            ),
        ),
        migrations.AddIndex(
            model_name="memetagging",
            index=models.Index(
                fields=["meme", "tag"], name="meme_taggin_meme_id_ff7b78_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="memetagging",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted_at__isnull", True)),
                fields=("meme", "tag"),
                name="unique_meme_tag",
            ),
        ),
    ]
