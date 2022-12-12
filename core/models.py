from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.IntegerField(default=-1)
    is_agent = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username


