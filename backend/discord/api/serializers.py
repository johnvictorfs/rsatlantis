from discord import models
from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.

    https://www.django-rest-framework.org/api-guide/serializers/#example
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class RaidsStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RaidsState
        fields = ('id', 'notifications', 'time_to_next_message')


class DisabledCommandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DisabledCommand
        fields = ('id', 'name')


class AmigoSecretoStateSerializer(serializers.HyperlinkedModelSerializer):
    registered = serializers.SerializerMethodField()

    @staticmethod
    def get_registered(obj):
        """
        Count the number of Users registered in the Discord's Secret Santa
        """
        return models.AmigoSecretoPerson.objects.all().count()

    class Meta:
        model = models.AmigoSecretoState
        fields = ('id', 'activated', 'registered', 'start_date', 'end_date', 'premio_minimo', 'premio_maximo')


class DiscordIngameNameSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.DiscordIngameName
        fields = ('user', 'name', 'created_date')


class DiscordUserSerializer(DynamicFieldsModelSerializer):
    # Get all the Ingame Names of a User
    ingame_names = DiscordIngameNameSerializer(many=True, read_only=True, fields=('name', 'created_date'))

    class Meta:
        model = models.DiscordUser
        fields = (
            'id', 'updated', 'warning_date', 'disabled', 'ingame_name', 'discord_id', 'discord_name', 'ingame_names'
        )


class AmigoSecretoPersonSerializer(serializers.HyperlinkedModelSerializer):
    user = DiscordUserSerializer(many=False, read_only=False, fields=('id', 'ingame_name', 'discord_name'))
    giving_to_user = DiscordUserSerializer(many=False, read_only=False, fields=('id', 'ingame_name', 'discord_name'))

    class Meta:
        model = models.AmigoSecretoPerson
        fields = ('id', 'user', 'giving_to_user', 'receiving')
