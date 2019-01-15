from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ingame_name = models.TextField(verbose_name='Nome no Jogo', max_length=12)
