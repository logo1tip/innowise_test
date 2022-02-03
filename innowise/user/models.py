from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    USER = "US"
    SUPPORT = "SP"
    ROLE = [
        (USER, "User"),
        (SUPPORT, "Support"),
    ]
    role = models.CharField(
        choices=ROLE,
        max_length=2,
        verbose_name="Role",
    )

    def __str__(self):
        return self.username


    class Meta:

        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["username"]
