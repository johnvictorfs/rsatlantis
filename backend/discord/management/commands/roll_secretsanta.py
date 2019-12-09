from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db.models import Q

from typing import List

from discord.models import AmigoSecretoState, AmigoSecretoPerson


class Command(BaseCommand):
    help = 'Make pairs for Secret Santa'

    def handle(self, *args, **options):
        now = timezone.now()
        secret_santa_state: AmigoSecretoState = AmigoSecretoState.object()

        if not secret_santa_state.end_date:
            raise CommandError('Sem data de sorteio configurada.')

        if secret_santa_state.end_date.date != now.date:
            raise CommandError(f'Secret santa is supposed to run only at {secret_santa_state.end_date}')

        not_receiving = AmigoSecretoPerson.objects.filter(receiving=False).count()

        if not_receiving == 0:
            self.stdout.write(self.style.ERROR('Nenhuma pessoa sem receber Presente, Amigo Secreto já está montado'))
            return

        while True:
            try:
                self.roll_secret_santa()
                break
            except Exception:
                self.stdout.write(self.style.ERROR('\nErro ao montar Amigo Secreto, limpando e tentando novamente\n'))
                self.clear_secret_santa()

        not_receiving = AmigoSecretoPerson.objects.filter(receiving=False).count()

        self.stdout.write(self.style.SUCCESS(f'\nAmigo Secreto montado com sucesso. Não recebendo: {not_receiving}'))

    @staticmethod
    def clear_secret_santa():
        AmigoSecretoPerson.objects.all().update(receiving=False, giving_to_user=None)

    def roll_secret_santa(self):
        exclude = []

        person: AmigoSecretoPerson
        for person in AmigoSecretoPerson.objects.filter(giving_to_user=None).all():
            random = self.random_person_to(person.id, exclude)

            self.stdout.write(
                self.style.SUCCESS(person.user.ingame_name) +
                ' is giving to ' +
                self.style.SUCCESS(random.user.ingame_name)
            )

            person.giving_to_user = random.user
            exclude.append(random.id)

    @staticmethod
    def random_person_to(pk: int, exclude: List[int]) -> AmigoSecretoPerson:
        """
        Get random entry for Secret Santa, excluding people already receiving presents and the person giving himself
        """

        random_person: AmigoSecretoPerson = AmigoSecretoPerson.objects.filter(
            receiving=False
        ).filter(
            Q(receiving=False) & ~Q(id=pk) & ~Q(id__in=exclude)
        ).order_by('?').first()

        if not random_person:
            pass

        random_person.receiving = True
        random_person.save()

        return random_person
