import random

import lorem
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from file_manager.models.thumbnail import Thumbnail
from meme.models.image_meme import ImageMeme
from meme.models.text_meme import TextMeme


class Command(BaseCommand):
    help = "Creates dummy memes for development and testing"

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            default=10,
            help="Total number of memes to create",
        )
        parser.add_argument(
            "--image",
            type=int,
            default=None,
            help="Number of image memes to create (takes precedence over total)",
        )
        parser.add_argument(
            "--text",
            type=int,
            default=None,
            help="Number of text memes to create (takes precedence over total)",
        )

    def handle(self, *args, **options):
        total_memes = options.get("number")
        image_memes_count = options.get("image")
        text_memes_count = options.get("text")

        if image_memes_count is not None or text_memes_count is not None:
            image_memes_count = image_memes_count or 0
            text_memes_count = text_memes_count or 0
        else:
            # Split the total between image and text memes
            image_memes_count = total_memes // 2
            text_memes_count = total_memes - image_memes_count

        User = get_user_model()

        # Create the specified number of image memes
        self.stdout.write(f"Creating {image_memes_count} image memes...")
        for i in range(image_memes_count):
            # Create a thumbnail for the image meme
            thumbnail = Thumbnail.objects.create(
                name=f"Dummy Thumbnail {i}",
                web_url="https://www.notion.so/image/attachment%3A84fd4666-fe81-4a5e-b3d3-93fdf1862654%3Aimage.png?table=block&id=1c245dc0-ef45-80cb-a963-d10964f31ec7&spaceId=9670d216-af32-4346-b6e8-3286d08ab53c&width=2000&userId=ddedc31a-d3a4-4262-a9fb-9d1fb5daf959&cache=v2",
            )

            # Create the image meme
            meme = ImageMeme.objects.create(
                title=f"Dummy Image Meme {i}",
                description=lorem.paragraph()[:100],
                creator=User.objects.first(),
                thumbnail=thumbnail,
                published_at=timezone.now() if random.choice([True, False]) else None,
            )

        # Create the specified number of text memes
        self.stdout.write(f"Creating {text_memes_count} text memes...")
        for i in range(text_memes_count):
            # Create the text meme
            meme = TextMeme.objects.create(
                title=f"Dummy Text Meme {i}",
                description=lorem.paragraph()[:100],
                creator=User.objects.first(),
                published_at=timezone.now() if random.choice([True, False]) else None,
            )

        created_memes = image_memes_count + text_memes_count
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {created_memes} dummy memes!")
        )
        self.stdout.write(f"- Image memes: {image_memes_count}")
        self.stdout.write(f"- Text memes: {text_memes_count}")
