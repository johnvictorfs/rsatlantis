from rest_framework import serializers

from discord.models import RaidsState, DisabledCommand, DiscordUser, AmigoSecretoPerson, AmigoSecretoState


class RaidsStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RaidsState
        fields = ('id', 'notifications', 'time_to_next_message')


class DisabledCommandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DisabledCommand
        fields = ('id', 'name')


class DiscordUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ('id', 'updated', 'warning_date', 'disabled', 'ingame_name', 'discord_id', 'discord_name')


class AmigoSecretoPersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmigoSecretoPerson
        fields = ('id', 'discord_id', 'discord_name', 'ingame_name', 'giving_to_id', 'giving_to_name', 'receiving')


class AmigoSecretoStateSerializer(serializers.HyperlinkedModelSerializer):
    registered = serializers.SerializerMethodField()

    @staticmethod
    def get_registered(obj):
        return AmigoSecretoPerson.objects.all().count()

    class Meta:
        model = AmigoSecretoState
        fields = ('id', 'activated', 'registered')
