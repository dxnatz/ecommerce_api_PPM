from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    is_banned = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        # Blocca l'accesso al login se bannato
        self.is_active = not self.is_banned

        super().save(*args, **kwargs)