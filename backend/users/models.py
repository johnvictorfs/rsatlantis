from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ingame_name = models.TextField(verbose_name='Nome no Jogo', max_length=12, blank=True)
    discord_id = models.BigIntegerField(verbose_name='ID do Discord', null=True)
