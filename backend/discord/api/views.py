from discord import models
from discord.api import permissions as discord_permissions
from discord.api import serializers
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


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


class DiscordIngameNameViewSet(viewsets.ModelViewSet):
    """
    Discord RS3 Ingame Names
    """
    serializer_class = serializers.DiscordIngameNameSerializer
    queryset = models.DiscordIngameName.objects.all()
    permission_classes = (discord_permissions.IsSuperUser,)
