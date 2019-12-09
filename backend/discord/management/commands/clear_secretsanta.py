from django.core.management.base import BaseCommand

from discord.models import AmigoSecretoPerson


class Command(BaseCommand):
    help = 'Clears receiving and giving_to fields on every Secret Santa entry'

    def handle(self, *args, **options):
        AmigoSecretoPerson.objects.all().update(receiving=False, giving_to_user=None)
        self.stdout.write(self.style.SUCCESS('Atualizado todos os campos do Amigo Secreto com sucesso.'))
