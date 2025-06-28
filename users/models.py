from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    is_banned = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # sincronizza is_active con is_banned
        self.is_active = not self.is_banned
        super().save(*args, **kwargs)