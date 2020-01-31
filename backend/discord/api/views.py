from discord import models
from discord.api import permissions as discord_permissions
from discord.api import serializers

import requests
from django.conf import settings
from requests_oauthlib import OAuth2Session
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


class StatusViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet for 'Status-based' ViewSets, that will have a '/status' endpoint action that will retrieve the
    first object from that Model in the DB
    """

    @action(detail=False, methods=['get'], permission_classes=[discord_permissions.AdminOrReadOnly])
    def status(self, request):
        """
        Returns the First Object from Model in DB, that will be the current Status of that Model
        """
        status = self.queryset.first()
        serializer = self.get_serializer(status)
        return Response(serializer.data)


class RaidsStateViewSet(StatusViewSet):
    """
    Get the Status of Raids stuff in Discord
    """
    serializer_class = serializers.RaidsStateSerializer
    queryset = models.RaidsState.objects.all()
    permission_classes = (discord_permissions.AdminOrReadOnly,)

    @action(detail=False, methods=['post'], permission_classes=[discord_permissions.AdminOrReadOnly])
    def toggle(self, request):
        """
        Toggle Status of Discord's Raids Notifications
        """
        raids_status = models.RaidsState.objects.first()
        raids_status.toggle()
        return Response('Status do Amigo Secreto atualizado com sucesso')


class DisabledCommandViewSet(viewsets.ModelViewSet):
    """
    Disabled Commands in Discord
    """
    serializer_class = serializers.DisabledCommandSerializer
    queryset = models.DisabledCommand.objects.all()
    permission_classes = (discord_permissions.AdminOrReadOnly,)


class DoacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoacaoSerializer
    queryset = models.Doacao.objects.all()
    permission_classes = (discord_permissions.AdminOrReadOnly,)


class DoacaoGoalViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoacaoGoalSerializer
    queryset = models.DoacaoGoal.objects.all()
    permission_classes = (discord_permissions.AdminOrReadOnly,)


class AmigoSecretoStatusViewSet(viewsets.ViewSet):
    """
    Discord's Secret Santa Status
    """
    queryset = models.AmigoSecretoState.objects.all()

    @staticmethod
    def list(request):
        """
        Get Secret Santa Status
        """
        secret_santa_status = models.AmigoSecretoState.object()

        if not secret_santa_status:
            # Create Status if it does not exist already
            secret_santa_status = models.AmigoSecretoState(activated=False)
            secret_santa_status.save()

        serializer = serializers.AmigoSecretoStateSerializer(secret_santa_status)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], permission_classes=[discord_permissions.AdminOrReadOnly])
    def update_dates(self, request):
        """
        Update Secret Santa Start and Date Dates
        """
        secret_santa_status = models.AmigoSecretoState.object()

        if not secret_santa_status:
            # Create status if it does not exist already
            secret_santa_status = models.AmigoSecretoState(activated=False)
            secret_santa_status.save()

        serializer = serializers.AmigoSecretoStateSerializer(data=request.data)

        if serializer.is_valid():
            # Update Start and End dates for Secret Santa
            secret_santa_status.start_date = serializer.data['start_date']
            secret_santa_status.end_date = serializer.data['end_date']
            secret_santa_status.save()

            return Response(serializers.AmigoSecretoStateSerializer(secret_santa_status).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[discord_permissions.AdminOrReadOnly])
    def toggle(self, request):
        """
        Toggle Status of Discord's Secret Santa
        """
        secret_santa_status = models.AmigoSecretoState.objects.first()
        secret_santa_status.toggle()
        return Response('Status do Amigo Secreto atualizado com sucesso')


class AmigoSecretoPersonViewSet(viewsets.ModelViewSet):
    """
    Discord's Secret Sant entries
    """
    serializer_class = serializers.AmigoSecretoPersonSerializer
    queryset = models.AmigoSecretoPerson.objects.all()
    permission_classes = (discord_permissions.IsSuperUser,)


class DiscordUserViewSet(viewsets.ModelViewSet):
    """
    Discord Users saved
    """
    serializer_class = serializers.DiscordUserSerializer
    queryset = models.DiscordUser.objects.all()
    permission_classes = (discord_permissions.AdminOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['$discord_name', '$ingame_name', '$ingame_names__name', 'discord_id', 'id']


class DiscordIngameNameViewSet(viewsets.ModelViewSet):
    """
    Discord RS3 Ingame Names
    """
    serializer_class = serializers.DiscordIngameNameSerializer
    queryset = models.DiscordIngameName.objects.all()
    permission_classes = (discord_permissions.IsSuperUser,)


class DiscordOauthAuthorizeView(APIView):
    @staticmethod
    def make_session(token=None, state=None, scope=None):
        return OAuth2Session(
            client_id=settings.DISCORD_OAUTH2_CLIENT_ID,
            token=token,
            state=state,
            scope=scope,
            redirect_uri=settings.DISCORD_OAUTH2_REDIRECT_URI,
            auto_refresh_kwargs={
                'client_id': settings.DISCORD_OAUTH2_CLIENT_ID,
                'client_secret': settings.DISCORD_OAUTH2_CLIENT_SECRET,
            },
            auto_refresh_url=settings.DISCORD_TOKEN_URL
        )

    def post(self, request, format=None):
        scope = ['identify', 'email', 'connections', 'guilds', 'guilds.join']

        discord = self.make_session(scope=scope)

        authorization_url, state = discord.authorization_url(settings.DISCORD_AUTHORIZATION_BASE_URL)

        print(authorization_url)
        print(state)

        return Response(
            {'state': state, 'authorization_url': authorization_url},
            status=status.HTTP_200_OK
        )


class DiscordUserOauthView(APIView):
    def post(self, request, format=None):
        data = {
            'client_id': settings.DISCORD_OAUTH2_CLIENT_ID,
            'client_secret': settings.DISCORD_OAUTH2_CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': request.data['code'],
            'redirect_uri': settings.DISCORD_OAUTH2_REDIRECT_URI,
            'scope': 'identify email connections'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        r = requests.post(f'{settings.DISCORD_API_BASE_URL}/oauth2/token', data=data, headers=headers)

        r.raise_for_status()
        return Response(r.json(), status=status.HTTP_200_OK)
