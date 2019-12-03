from django.utils import timezone
from django.db import models


class DiscordManager(models.Manager):
    """
    Model Manager that will use the 'use_db' attribute from Model if it exists

    Used to set the Db used to be the Discord one

    https://stackoverflow.com/a/55754529/10416161
    """

    def get_queryset(self):
        qs = super().get_queryset()

        # if `use_db` is set on model use that for choosing the DB
        if hasattr(self.model, 'use_db'):
            qs = qs.using(self.model.use_db)

        return qs


class DiscordModel(models.Model):
    """
    Set up 'discord' DB to be used for Model
    """
    use_db = 'discord'
    objects = DiscordManager()

    class Meta:
        abstract = True


class RaidsState(DiscordModel):
    notifications = models.BooleanField(verbose_name='Notificações', default=False)
    time_to_next_message = models.TextField(verbose_name='Próxima Mensagem', null=True)

    class Meta:
        db_table = 'raidsstate'

    def toggle(self):
        self.notifications = not self.notifications
        self.save()


class DisabledCommand(DiscordModel):
    name = models.TextField(verbose_name='Nome', unique=True)

    class Meta:
        db_table = 'disabled_command'


class AmigoSecretoPerson(DiscordModel):
    discord_id = models.TextField(verbose_name='ID Discord', unique=True)
    discord_name = models.TextField(verbose_name='Nome Discord')
    ingame_name = models.TextField(verbose_name='Nome RuneScape')
    giving_to_id = models.IntegerField(null=True, default=None, unique=True)
    giving_to_name = models.TextField(null=True, default=None, unique=True)
    receiving = models.BooleanField(default=False)

    class Meta:
        db_table = 'amigosecreto'


class AmigoSecretoState(DiscordModel):
    activated = models.BooleanField(default=False)

    class Meta:
        db_table = 'amigosecretostate'

    def toggle(self):
        self.activated = not self.activated
        self.save()


class DiscordUser(DiscordModel):
    updated = models.DateTimeField(default=timezone.now)
    warning_date = models.DateTimeField(null=True)
    disabled = models.BooleanField(default=False)
    ingame_name = models.TextField(unique=True, null=False)
    discord_id = models.TextField()
    discord_name = models.TextField()

    class Meta:
        db_table = 'user'


class DiscordIngameName(DiscordModel):
    name = models.TextField(verbose_name='Nome RuneScape')
    user = models.ForeignKey(
        verbose_name='Usuário', to=DiscordUser, related_name='ingame_names', on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'ingame_name'
