from random import randint

from django.db import models
from django.db.models.aggregates import Count
from django.utils import timezone


class DiscordManager(models.Manager):
    def get_queryset(self):
        """
        Uuse the 'use_db' attribute from Model if it exists

        Used to set the Db used to be the Discord one

        https://stackoverflow.com/a/55754529/10416161
        """
        qs = super().get_queryset()

        # if `use_db` is set on model use that for choosing the DB
        if hasattr(self.model, 'use_db'):
            qs = qs.using(self.model.use_db)

        return qs

    def random(self):
        """
        Get random object from database

        https://stackoverflow.com/a/2118712/10416161
        """
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)

        return self.all()[random_index]


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

    @classmethod
    def object(cls):
        # Get the First Item
        item = cls._default_manager.all().first()

        # Create Item if one does not exist
        if not item:
            item = cls._default_manager.create(notifications=False)
            item.save()

        return item

    def save(self, *args, **kwargs):
        """
        https://stackoverflow.com/a/54722087/10416161
        """
        # Can't create more than one of the Model
        self.id = 1
        return super().save(*args, **kwargs)


class DisabledCommand(DiscordModel):
    name = models.TextField(verbose_name='Nome', unique=True)

    class Meta:
        db_table = 'disabled_command'


class AmigoSecretoState(DiscordModel):
    activated = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    premio_minimo = models.BigIntegerField(null=True)
    premio_maximo = models.BigIntegerField(null=True)

    class Meta:
        db_table = 'amigosecretostate'

    def toggle(self):
        self.activated = not self.activated
        self.save()

    @classmethod
    def object(cls):
        # Get the First Item
        item = cls._default_manager.all().first()

        # Create Item if one does not exist
        if not item:
            item = cls._default_manager.create(activated=False)
            item.save()

        return item

    def save(self, *args, **kwargs):
        """
        https://stackoverflow.com/a/54722087/10416161
        """
        # Can't create more than one of the Model
        self.id = 1
        return super().save(*args, **kwargs)


class DiscordUser(DiscordModel):
    updated = models.DateTimeField(default=timezone.now)
    warning_date = models.DateTimeField(null=True)
    disabled = models.BooleanField(default=False)
    ingame_name = models.TextField(unique=True, null=False)
    discord_id = models.TextField()
    discord_name = models.TextField()

    class Meta:
        db_table = 'user'


class AmigoSecretoPerson(DiscordModel):
    user = models.ForeignKey(
        to=DiscordUser,
        verbose_name='Usuário',
        related_name='discord_user',
        on_delete=models.CASCADE
    )

    giving_to_user = models.ForeignKey(
        to=DiscordUser,
        verbose_name='Presenteando',
        related_name='giving_to_discord_user',
        on_delete=models.CASCADE,
        null=True
    )

    receiving = models.BooleanField(default=False)

    class Meta:
        db_table = 'amigosecreto'

    def save(self, *args, **kwargs):
        """
        Prevent user from rolling himself on Secret Santa
        """
        if self.user == self.giving_to_user:
            raise Exception('Um Usuário não pode presentear a si mesmo')

        super(AmigoSecretoPerson, self).save(*args, **kwargs)


class DiscordIngameName(DiscordModel):
    name = models.TextField(verbose_name='Nome RuneScape')
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        to=DiscordUser,
        verbose_name='Usuário',
        related_name='ingame_names',
        db_column='user',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'ingame_name'
