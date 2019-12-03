import Service from '@/api/service'
import { Api } from '@/api'
import { IPlayer } from '@/types'

export default class PlayerService extends Service {
  public async all(): Promise<IPlayer[]> {
    /**
     * Get all Players
     */
    const { data } = await this.api.axios.get('players')
    return data
  }

  public async get(name: string): Promise<IPlayer> {
    /**
     * Get specific Player by Name
     */
    const { data } = await this.api.axios.get(`players/${name}`)
    return data
  }
}
