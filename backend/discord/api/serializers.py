from rest_framework import serializers

from discord.models import RaidsState, DisabledCommand, DiscordUser, AmigoSecretoPerson, AmigoSecretoState


class RaidsStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RaidsState
        fields = ('notifications', 'time_to_next_message')


class DisabledCommandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DisabledCommand
        fields = ('name',)


class DiscordUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ('updated', 'warning_date', 'disabled', 'ingame_name', 'discord_id', 'discord_name')


class AmigoSecretoPersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmigoSecretoPerson
        fields = ('discord_id', 'discord_name', 'ingame_name', 'giving_to_id', 'giving_to_name', 'receiving')


class AmigoSecretoStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmigoSecretoState
        fields = ('activated',)
