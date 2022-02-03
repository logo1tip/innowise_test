from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import CustomUser


class AdminUser(UserAdmin):

    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "role",
    )
    list_display_links = (
        "id",
        "username",
    )
    list_filter = (
        "username",
        "last_name", 
        "role",
    )
    ordering = (
        "username",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "password",
                    "role",
                )
            },
        ),
    )


admin.site.register(CustomUser, AdminUser)