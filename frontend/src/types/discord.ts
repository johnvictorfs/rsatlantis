export interface Discord {
  RaidsStatus: {
    notifications: boolean
    timeToNextMessage: string
  }

  DiscordUser: {
    id: number
    updated?: string
    warningDate?: string
    disabled: boolean
    ingameName: string
    discordId: number
    discordName: string
  }

  SecretSantaStatus: {
    activated: boolean
    registered: number
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
  game?: {
    name: string
  }
}

export interface DiscordApi {
  RaidsStatus: {
    id: number
    notifications: boolean
    time_to_next_message: string
  }

  DiscordUser: {
    id: number
    updated?: string
    warning_date?: string
    disabled: boolean
    ingame_name: string
    discord_id: string
    discord_name: string
  }

  SecretSantaStatus: {
    activated: boolean
    registered: number
  }

  Widget: {
    id: string
    name: string
    instant_invite: string
    channels: DiscordChannel[]
    members: DiscordMember[]
  }
}
