from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from discord import models
from discord.api import serializers, permissions as discord_permissions


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
        status = models.RaidsState.objects.first()
        status.toggle()
        return Response('Status do Amigo Secreto atualizado com sucesso')


class DisabledCommandViewSet(viewsets.ModelViewSet):
    """
    Disabled Commands in Discord
    """
    serializer_class = serializers.DisabledCommandSerializer
    queryset = models.DisabledCommand.objects.all()
    permission_classes = (discord_permissions.AdminOrReadOnly,)


class AmigoSecretoPersonViewSet(viewsets.ModelViewSet):
    """
    Discord's Secret Sant entries
    """
    serializer_class = serializers.AmigoSecretoPersonSerializer
    queryset = models.AmigoSecretoPerson.objects.all()
    permission_classes = (discord_permissions.IsSuperUser,)

    @action(detail=False, methods=['get'], permission_classes=[discord_permissions.AdminOrReadOnly])
    def status(self, request):
        """
        Current Discord's Secret Santa status
        """
        status = models.AmigoSecretoState.objects.first()
        serializer = serializers.AmigoSecretoStateSerializer(status)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], permission_classes=[discord_permissions.AdminOrReadOnly])
    def toggle(self, request):
        """
        Toggle Status of Discord's Secret Santa
        """
        status = models.AmigoSecretoState.objects.first()
        status.toggle()
        return Response('Status do Amigo Secreto atualizado com sucesso')


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
