import re
import json

import requests
from django.db import models


class ClanMember(models.Model):
    name = models.TextField(verbose_name='Nome', max_length=12)
    exp = models.FloatField()
    rank = models.TextField()

    def is_in_clan(self) -> bool:
        """
        Grabs player details from RuneScape's API and verifies if the user is in the clan 'Atlantis'
        """
        details = self.get_player_details()
        parsed = self.parse_player_details(details)
        if parsed.get('clan') == 'Atlantis':
            return True
        return False

    def get_player_details(self) -> str:
        """
        Gets the player details from RuneScape's API in the format below:

        jQuery000000000000000_0000000000([{"isSuffix":false,"recruiting":true,"name":"nriver","clan":"Atlantis","title":""}]);

        Has to be parsed before usage with ClanMember.parse_player_details()
        """
        base_url = "http://services.runescape.com/m=website-data/"
        url = f"{base_url}playerDetails.ws?names=%5B%22{self.name}%22%5D&callback=jQuery000000000000000_0000000000&_=0"
        r = requests.get(url)
        if r.status_code == 200:
            return str(r.content)

    @staticmethod
    def parse_player_details(details: str) -> dict:
        """
        Parses the string representation of the player's details, grabbed from RuneScape's API, and returns in dict
        """
        # Searchs for everything inside curly brackets -> {}
        parsed = re.search(r'{([^)]+)\}', details)
        if parsed:
            parsed = parsed.group()
            return json.loads(parsed)
        return {}
