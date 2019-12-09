export interface Discord {
  RaidsStatus: {
    notifications: boolean
    timeToNextMessage: string
  }

  DiscordUser: {
    id: number
    updated: string | null
    warningDate: string | null
    disabled: boolean
    ingameName: string
    discordId: number
    discordName: string
  }

  SecretSantaStatus: {
    activated: boolean
    registered: number
    startDate: string | null
    endDate: string | null
    premioMinimo: number | null
    premioMaximo: number | null
  }
}

export interface DiscordChannel {
  id: string
  name: string
  position: number
}

export interface DiscordMember {
  id: string
  username: string
  avatar: string
  discriminator: string
  status: string
  avatar_url: string
  game: {
    name: string
  } | null
}

export interface DiscordApi {
  RaidsStatus: {
    id: number
    notifications: boolean
    time_to_next_message: string
  }

  DiscordUser: {
    id: number
    updated: string | null
    warning_date: string | null
    disabled: boolean
    ingame_name: string
    discord_id: string
    discord_name: string
  }

  SecretSantaStatus: {
    activated: boolean
    registered: number
    start_date: string | null
    end_date: string | null
    premio_minimo: number | null
    premio_maximo: number | null
  }

  Widget: {
    id: string
    name: string
    instant_invite: string
    channels: DiscordChannel[]
    members: DiscordMember[]
  }
}
