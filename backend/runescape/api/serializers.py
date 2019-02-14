from rest_framework import serializers

from runescape.models import ClanMember


class ClanMemberSerializer(serializers.HyperlinkedModelSerializer):
    translated_rank = serializers.SerializerMethodField()

    @staticmethod
    def get_translated_rank(obj):
        ranks = {
            "Owner": "Líder",
            "Deputy Owner": "Vice-Líder",
            "Overseer": "Fiscal",
            "Coordinator": "Coordenador",
            "Organiser": "Organizador",
            "Admin": "Admin",
            "General": "General",
            "Captain": "Capitão",
            "Lieutenant": "Tenente",
            "Sergeant": "Sargento",
            "Corporal": "Cabo",
            "Recruit": "Recruta"
        }
        return ranks[obj.rank]

    class Meta:
        model = ClanMember
        fields = ('url', 'name', 'exp', 'rank', 'translated_rank')
        read_only_fields = ('url', 'name', 'exp', 'rank')
        extra_kwargs = {'url': {'lookup_field': 'name'}}
