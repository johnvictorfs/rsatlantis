import json

from django.test import TestCase
from runescape.models import ClanMember


class ClanMemberTestCase(TestCase):
    def setUp(self):
        ClanMember.objects.create(name='NRiver', exp=0, rank='Overseer')

    def test_parse_player_details(self):
        """
        Tests if the ClanMember.parse_player_details() method correctly parses data usually grabbed from
        RuneScape's API and returns the data in the correct format to be used
        """
        result = '{"isSuffix":false,"recruiting":true,"name":"NRiver","clan":"Atlantis","title":""}'
        details = f'jQuery000000000000000_0000000000([{result}]);'
        parsed = json.loads(result)
        member: ClanMember = ClanMember.objects.first()
        self.assertEqual(member.parse_player_details(details), parsed)
        self.assertEqual(member.parse_player_details(details).get('clan'), 'Atlantis')

    def test_outdated_rank(self):
        member = ClanMember(name='NRiver', exp=1200_000_000, rank='Sergeant')
        self.assertTrue(member.outdated_rank())
        member.exp = 10_000_000
        self.assertFalse(member.outdated_rank())
