import csv

import requests
from django.core.management.base import BaseCommand, CommandError
from runescape.models import ClanMember


class Command(BaseCommand):
    help = "Updates all Clan Members info using RuneScape's API"

    def handle(self, *args, **options):
        clan_list = self.parsed_clan_list(self.grab_clan_list())

        # Updating the details of every clan member in the database, or creating new entries for new Clan Members
        for member_name, member_rank, member_exp in clan_list[1:]:
            # Format of 'member': ['Clanmate', 'Clan Rank', 'Total XP', 'Kills']
            ClanMember.objects.update_or_create(
                player_name=member_name,
                defaults={
                    'exp': member_exp,
                    'rank': member_rank,
                    'active': True
                }
            )

        clan_name_list = set(clan_member[0] for clan_member in clan_list)

        # Setting clan members no longer in the clan (or changed names) as inactive
        for member in ClanMember.objects.all():
            if member.player_name not in clan_name_list:
                member.active = False
                member.save()

        self.stdout.write(self.style.SUCCESS('Membros do Clã atualizados com sucesso.'))

    @staticmethod
    def grab_clan_list():
        clan_url = 'http://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName=Atlantis'
        with requests.Session() as session:
            download = session.get(clan_url)
            decoded = download.content.decode('windows-1252')
            if download.status_code != 200:
                raise CommandError(f'Não foi possível se conectar com a API do RuneScape ({download.status_code})')
            return decoded

    @staticmethod
    def parsed_clan_list(clan_list) -> list:
        parsed_list = list(csv.reader(clan_list.splitlines(), delimiter=','))

        if parsed_list[0][0] != 'Clanmate':
            raise CommandError('Lista de Membros do clã inválida.')

        for row in parsed_list:
            # Remove non-breaking spaces
            row[0] = row[0].replace(r'\xa0', ' ')

        return parsed_list
