# Generated by Django 5.1.5 on 2025-03-21 09:42

import user.models.user
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", user.models.user.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="deleted_at",
        ),
    ]
