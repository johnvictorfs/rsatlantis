import Service from '@/api/service'
import { Api } from '@/api'
import { IPlayer, Discord, DiscordApi } from '@/types'

export default class DiscordService extends Service {
  public raids: RaidsService
  public secretSanta: SecretSantaService

  constructor(api: Api) {
    super(api)

    this.raids = new RaidsService(api)
    this.secretSanta = new SecretSantaService(api)
  }

  public async users(): Promise<Discord['DiscordUser'][]> {
    /**
     * Get all Discord authenticated Users
     */
    const { data }: { data: DiscordApi['DiscordUser'][] } = await this.api.axios.get('discord/users')

    return data.map(user => ({
      id: user.id,
      updated: user.updated,
      warningDate: user.warning_date,
      disabled: user.disabled,
      ingameName: user.ingame_name,
      discordId: Number.parseInt(user.discord_id),
      discordName: user.discord_name
    }))
  }

  public async user(id: number): Promise<Discord['DiscordUser'] | null> {
    /**
     * Get specific Discord Authenticated User by ID
     */
    const { data: user }: { data: DiscordApi['DiscordUser'] } = await this.api.axios.get(`discord/users/${id}`)

    if (!user) return null

    return {
      id: user.id,
      updated: user.updated,
      warningDate: user.warning_date,
      disabled: user.disabled,
      ingameName: user.ingame_name,
      discordId: Number.parseInt(user.discord_id),
      discordName: user.discord_name
    }
  }

  public async widget(): Promise<DiscordApi['Widget']> {
    const url = 'https://discordapp.com/api/guilds/321012107942428673/widget.json'
    const { data }: { data: DiscordApi['Widget'] } = await this.api.axios.get(url)
    return data
  }
}

class RaidsService extends Service {
  public async status(): Promise<Discord['RaidsStatus']> {
    /**
     * Get the current Status of Raids Notifications on Discord
     */
    const { data }: { data: DiscordApi['RaidsStatus'] } = await this.api.axios.get('discord/raids/status')
    return { notifications: data.notifications, timeToNextMessage: data.time_to_next_message }
  }

  public async toggle(): Promise<void> {
    /**
     * Toggle status of Discord's Raids notifications
     */
    await this.api.axios.post('discord/raids/toggle')
  }
}

class SecretSantaService extends Service {
  public async status(): Promise<Discord['SecretSantaStatus']> {
    /**
     * Get current status of Discord's Secret Santa
     */
    const { data }: { data: DiscordApi['SecretSantaStatus'] } = await this.api.axios.get('discord/amigosecreto_status')
    return {
      startDate: data.start_date,
      endDate: data.end_date,
      activated: data.activated,
      registered: data.registered,
      premioMaximo: data.premio_maximo,
      premioMinimo: data.premio_minimo
    }
  }

  public async users(): Promise<DiscordApi['SecretSantaUser'][]> {
    /**
     * Get currently registered Secret Santa Users
     */
    const { data }: { data: DiscordApi['SecretSantaUser'][] } = await this.api.axios.get('discord/amigosecreto')
    return data
  }

  public async toggle(): Promise<void> {
    /**
     * Toggle status of Discord's Secret Santa
     */
    await this.api.axios.post('discord/amigosecreto_status/toggle')
  }

  public async updateDates(startDate: string, endDate: string, premioMinimo: string): Promise<Discord['SecretSantaStatus']> {
    /**
     * Update Discord's Secret Santa Start and End Dates
     */

    const { data }: { data: DiscordApi['SecretSantaStatus'] } = await this.api.axios.post(
      'discord/amigosecreto_status/update_dates',
      {
        start_date: startDate,
        end_date: endDate,
        premio_minimo: Number.parseInt(premioMinimo)
      }
    )

    return {
      startDate: data.start_date,
      endDate: data.end_date,
      activated: data.activated,
      registered: data.registered,
      premioMinimo: data.premio_minimo,
      premioMaximo: data.premio_maximo
    }
  }
}
