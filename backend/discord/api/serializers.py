from rest_framework import serializers

from discord.models import RaidsState, DisabledCommand, DiscordUser, AmigoSecretoPerson, AmigoSecretoState, \
    DiscordIngameName


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
        model = RaidsState
        fields = ('id', 'notifications', 'time_to_next_message')


class DisabledCommandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DisabledCommand
        fields = ('id', 'name')


class AmigoSecretoPersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmigoSecretoPerson
        fields = ('id', 'user', 'giving_to_user', 'receiving')


class AmigoSecretoStateSerializer(serializers.HyperlinkedModelSerializer):
    registered = serializers.SerializerMethodField()

    @staticmethod
    def get_registered(obj):
        return AmigoSecretoPerson.objects.all().count()

    class Meta:
        model = AmigoSecretoState
        fields = ('id', 'activated', 'registered', 'start_date', 'end_date')


class DiscordIngameNameSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = DiscordIngameName
        fields = ('user', 'name', 'created_date')


class DiscordUserSerializer(serializers.ModelSerializer):
    ingame_names = DiscordIngameNameSerializer(many=True, read_only=True, fields=('name', 'created_date'))

    class Meta:
        model = DiscordUser
        fields = ('updated', 'warning_date', 'disabled', 'ingame_name', 'discord_id', 'discord_name', 'ingame_names')
