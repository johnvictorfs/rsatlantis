import json
import re

import requests
from django.db import models
from dynamic_preferences.registries import global_preferences_registry


class ClanMember(models.Model):
    rank_choices = (
        ('Recruit', 'Recruta'),
        ('Corporal', 'Cabo'),
        ('Lieutenant', 'Tenente'),
        ('Captain', 'Capitão'),
        ('General', 'General'),
        ('Admin', 'Administrador'),
        ('Organiser', 'Organizador'),
        ('Coordinator', 'Coordenador'),
        ('Overseer', 'Fiscal'),
        ('Deputy Owner', 'Vice-Líder'),
        ('Owner', 'Líder')
    )

    name = models.TextField(verbose_name='Nome', max_length=12)
    exp = models.FloatField()
    rank = models.TextField(choices=rank_choices)

    def __str__(self):
        return self.name

    def is_in_clan(self) -> bool:
        """
        Grabs player details from RuneScape's API and verifies if the user is in the clan 'Atlantis'
        """
        details = self.get_player_details()
        parsed = self.parse_player_details(details)
        if parsed.get('clan') == 'Atlantis':
            return True
        return False

    def outdated_rank(self) -> bool:
        """
        Verifies if a Clan Member requires a rank promotion based on their Clan Exp

        Will return True if the Member has a rank Higher than he needs to be based on their Exp

        Will return True regardless of Exp if the Member has an administrative rank
        """
        if self.rank in ['Admin', 'Organiser', 'Coordinator', 'Coordinator', 'Overseer', 'Deputy Owner', 'Owner']:
            return True

        rank_value = {
            'Recruit': 0,
            'Corporal': 1,
            'Sergeant': 2,
            'Lieutenant': 3,
            'Captain': 4,
            'General': 5
        }

        rank = self.exp_rank()

        # Returns False if the member's rank is higher than the rank he needs to be based on exp
        # That way early rank-ups will not throw a false-positive
        if rank_value[self.rank] > rank_value[rank]:
            return False

        return self.rank != rank

    def exp_rank(self) -> str:
        """
        Checks which rank the Clan Member is supposed to be based solely on their Clan Exp, disregarding
        administrative ranks
        """
        rank = 'Recruit'

        global_preferences = global_preferences_registry.manager()
        if self.exp >= global_preferences['clan_ranks__corporal_exp']:
            rank = 'Corporal'
        if self.exp >= global_preferences['clan_ranks__sergeant_exp']:
            rank = 'Sergeant'
        if self.exp >= global_preferences['clan_ranks__lieutenant_exp']:
            rank = 'Lieutenant'
        if self.exp >= global_preferences['clan_ranks__captain_exp']:
            rank = 'Captain'
        if self.exp >= global_preferences['clan_ranks__general_exp']:
            rank = 'General'

        return rank

    def get_player_details(self) -> str:
        """
        Gets the player details from RuneScape's API in the format below:

        jQuery000000000000000_0000000000([{"isSuffix":false,"recruiting":true,"name":"nriver","clan":"Atlantis","title":""}]);

        Has to be parsed before usage with ClanMember.parse_player_details()
        """
        base_url = 'http://services.runescape.com/m=website-data/'
        url = f'{base_url}playerDetails.ws?names=%5B%22{self.name}%22%5D&callback=jQuery000000000000000_0000000000&_=0'
        r = requests.get(url)

        if r.status_code == 200:
            return str(r.content)
        return ''

    @staticmethod
    def parse_player_details(details: str) -> dict:
        """
        Parses the string representation of the player's details, grabbed from RuneScape's API, and returns in dict
        """
        parsed = re.search(r'{([^)]+)}', details)  # Searchs for everything inside curly brackets -> {}
        if parsed:
            return json.loads(parsed.group())
        return {}
