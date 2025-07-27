from bookmark.models import Bookmark, Bookmarking
from django.db.models.signals import post_save
from drf_spectacular.utils import OpenApiExample, extend_schema
from meme.models import Meme
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from tag.tasks.tag_counter_tasks import update_counters_for_bookmarking


class BookmarkingSyncAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="bulk sync bookmarkings",
        description=("단일 밈과 여러 북마크에 대해서 동시에 다룹니다."),
        operation_id="bookmarking_sync",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "meme_id": {
                        "type": "integer",
                        "description": "The ID of the Meme to sync.",
                    },
                    "bookmark_ids": {
                        "type": "array",
                        "items": {"type": "integer"},
                        "description": "List of Bookmark IDs belonging to the user.",
                    },
                },
                "required": ["meme_id", "bookmark_ids"],
            }
        },
        responses={
            200: {
                "description": "Successful synchronization.",
                "content": {
                    "application/json": {
                        "example": {"detail": "Bookmarkings synced successfully."}
                    }
                },
            },
            400: {
                "description": "Bad Request (e.g. missing fields).",
                "content": {
                    "application/json": {
                        "example": {"detail": "meme_id and bookmark_ids are required."}
                    }
                },
            },
            404: {
                "description": "Meme not found or invalid resource.",
                "content": {"application/json": {"example": {"detail": "Not found."}}},
            },
        },
        tags=["bookmarking"],
        examples=[
            OpenApiExample(
                "Example",
                summary="A valid request",
                value={"meme_id": 10, "bookmark_ids": [101, 102, 103]},
            )
        ],
    )
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        meme_id = data.get("meme_id")
        bookmark_ids = data.get("bookmark_ids", [])

        if not meme_id:
            return Response(
                {"detail": "meme_id is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        meme = get_object_or_404(Meme, pk=meme_id)

        valid_bookmark_ids = set(
            Bookmark.objects.filter(user=user, pk__in=bookmark_ids).values_list(
                "id", flat=True
            )
        )

        if len(valid_bookmark_ids) != len(bookmark_ids) or set(
            valid_bookmark_ids
        ) != set(bookmark_ids):
            return Response(
                {"detail": "Invalid resource."}, status=status.HTTP_400_BAD_REQUEST
            )

        existing_bookmark_ids = set(
            Bookmarking.objects.filter(user=user, meme=meme).values_list(
                "bookmark_id", flat=True
            )
        )

        to_remove = existing_bookmark_ids - valid_bookmark_ids
        to_add = valid_bookmark_ids - existing_bookmark_ids

        if to_remove:
            Bookmarking.objects.filter(
                user=user, meme=meme, bookmark_id__in=to_remove
            ).delete()

        new_objects = []
        for bk_id in to_add:
            new_objects.append(Bookmarking(meme=meme, bookmark_id=bk_id, user=user))

        if new_objects:
            created_objects = Bookmarking.objects.bulk_create(new_objects)

            bookmark_ids = [obj.bookmark_id for obj in created_objects]
            refreshed_objects = Bookmarking.objects.filter(
                bookmark_id__in=bookmark_ids, meme=meme, user=user
            ).select_related("bookmark", "meme")

            for obj in refreshed_objects:
                post_save.send(sender=Bookmarking, instance=obj, created=True)

        if to_remove:
            update_counters_for_bookmarking.delay(user.id, meme.id)

        return Response(
            {"detail": "Bookmarkings synced successfully."}, status=status.HTTP_200_OK
        )
