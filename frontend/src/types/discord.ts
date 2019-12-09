export interface Discord {
  RaidsStatus: {
    notifications: boolean
    timeToNextMessage: string
  }

  DiscordUser: {
    id: number
<<<<<<< HEAD
    updated?: string
    warningDate?: string
=======
    updated: string | null
    warningDate: string | null
>>>>>>> d0f5c5527e7cb58e908630f686b0338aa1adaeb1
    disabled: boolean
    ingameName: string
    discordId: number
    discordName: string
  }

  SecretSantaStatus: {
    activated: boolean
    registered: number
<<<<<<< HEAD
=======
    startDate: string | null
    endDate: string | null
    premioMinimo: number | null
    premioMaximo: number | null
>>>>>>> d0f5c5527e7cb58e908630f686b0338aa1adaeb1
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
<<<<<<< HEAD
  game?: {
    name: string
  }
=======
  game: {
    name: string
  } | null
>>>>>>> d0f5c5527e7cb58e908630f686b0338aa1adaeb1
}

export interface DiscordApi {
  RaidsStatus: {
    id: number
    notifications: boolean
    time_to_next_message: string
  }

  DiscordUser: {
    id: number
<<<<<<< HEAD
    updated?: string
    warning_date?: string
=======
    updated: string | null
    warning_date: string | null
>>>>>>> d0f5c5527e7cb58e908630f686b0338aa1adaeb1
    disabled: boolean
    ingame_name: string
    discord_id: string
    discord_name: string
  }

  SecretSantaStatus: {
    activated: boolean
    registered: number
<<<<<<< HEAD
=======
    start_date: string | null
    end_date: string | null
    premio_minimo: number | null
    premio_maximo: number | null
>>>>>>> d0f5c5527e7cb58e908630f686b0338aa1adaeb1
  }

  Widget: {
    id: string
    name: string
    instant_invite: string
    channels: DiscordChannel[]
    members: DiscordMember[]
  }
}
