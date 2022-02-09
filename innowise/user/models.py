from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse


class CustomUser(AbstractUser):

    class UserRole(models.TextChoices):
        USER = "US", _("User")
        SUPPORT = "SP", _("Support")

    role = models.CharField(
        max_length=2,
        choices=UserRole.choices,
        default=UserRole.SUPPORT,
    )
    
    def get_absolute_url(self):
        return reverse("user", kwargs={"id": self.id, "name": self.username})
    
    def __str__(self):
        return self.username


    class Meta:

        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["username"]
