from rest_framework import viewsets
from runescape.api.permissions import ReadOnly
from runescape.api.serializers import ClanMemberSerializer
from runescape.models import ClanMember


class ClanMemberViewSet(viewsets.ModelViewSet):
    serializer_class = ClanMemberSerializer
    lookup_field = 'player_name'
    queryset = ClanMember.objects.filter(active=True)
    permission_classes = (ReadOnly,)
