import { Api } from './index'
import { IPlayer } from '@/types'

export default class PlayerService {
  private api: Api

  constructor(api: Api) {
    this.api = api
  }

  async all(): Promise<IPlayer[]> {
    /**
     * Get all Players
     */
    const { data } = await this.api.axios.get('players')
    return data
  }

  async get(name: string): Promise<IPlayer> {
    /**
     * Get specific Player by Name
     */
    const { data } = await this.api.axios.get(`players/${name}`)
    return data
  }
}
