from django.contrib import admin
from task.models import Post, Comment


class AdminPost(admin.ModelAdmin):
    list_display = (
        "title", 
        "author",
        "status",
        "created",
    )
    list_filter = (
        "title",
        "status",
    )


class AdminComment(admin.ModelAdmin):
    list_display = (
        "post", 
        "author",
        "created",
    )


admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)

