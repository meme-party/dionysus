# Generated by Django 5.1.7 on 2025-03-28 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_user_username"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserTagCounter",
        ),
    ]
