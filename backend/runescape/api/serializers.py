from rest_framework import serializers

from runescape.models import ClanMember


class ClanMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClanMember
        fields = ('url', 'name', 'exp', 'rank')
        read_only_fields = ('url', 'name', 'exp', 'rank')
        extra_kwargs = {'url': {'lookup_field': 'name'}}
