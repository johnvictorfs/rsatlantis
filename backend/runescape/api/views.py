from rest_framework import viewsets
from runescape.api.permissions import ReadOnly
from runescape.api.serializers import ClanMemberSerializer
from runescape.models import ClanMember


class ClanMemberViewSet(viewsets.ModelViewSet):
    serializer_class = ClanMemberSerializer
    lookup_field = 'name'
    queryset = ClanMember.objects.all()
    permission_classes = (ReadOnly,)
