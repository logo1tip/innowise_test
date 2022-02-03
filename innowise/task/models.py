from django.db import models

from user.models import CustomUser


class Post(models.Model):

    SOLVED = "SD"
    UNRESOLVED = "UNSD"
    FROZEN = "FR"

    STATUS = [
        (SOLVED, "Solved"),
        (UNRESOLVED, "Unresolved"),
        (FROZEN, "Frozen"),
    ]

    title = models.CharField(
        max_length=255,
    )
    text = models.TextField()
    author = models.ForeignKey(
        CustomUser,
        related_name="posts",
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        choices=STATUS,
        max_length=5,
        default="SD",
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )


    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["created"]

    def __str__(self):
        return f"Coments of {self.author}"


class Comment(models.Model):
    
    author = models.ForeignKey(
        CustomUser,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    text = models.TextField(
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )


    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


