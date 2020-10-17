from discord.models import (
    AmigoSecretoPerson,
    AmigoSecretoState,
    DisabledCommand,
    DiscordIngameName,
    DiscordUser,
    RaidsState
)
from django.contrib import admin

admin.site.register(AmigoSecretoState)
admin.site.register(AmigoSecretoPerson)
admin.site.register(DiscordUser)
admin.site.register(DisabledCommand)
admin.site.register(DiscordIngameName)
admin.site.register(RaidsState)
