import { Api } from './index'
import { IGuide, IGuideWithAuthor, IUser } from '@/types'

export default class GuideService {
  private api: Api

  constructor(api: Api) {
    this.api = api
  }

  private async getAuthor(url: string): Promise<IUser | null> {
    /**
     * Get the Author User from an author API URI and returns it, if it exists, or null, otherwise
     *
     * Also return null if GET request to the Author's URI fails for any reason
     */
    try {
      const { data } = await this.api.axios.get(url)
      return data
    } catch (error) {
      return null
    }
  }

  async all(): Promise<IGuideWithAuthor[]> {
    /**
     * Get all Guides
     */
    const { data }: { data: IGuideWithAuthor[] } = await this.api.axios.get('guides')

    for (const guide of data) {
      guide.getAuthor = async () => {
        const author = await this.getAuthor(guide.author as string)
        return author
      }
    }

    return data
  }

  async get(slug: string): Promise<IGuideWithAuthor> {
    /**
     * Get specific Guide by Slug
     */
    const { data } = await this.api.axios.get(`guides/${slug}`)

    const getAuthor = async () => {
      const author = await this.getAuthor(data.author)
      return author
    }

    return { ...data, getAuthor }
  }

  async delete(slug: string): Promise<void> {
    /**
     * Delete Guide by Slug
     */
    await this.api.axios.delete(`guides/${slug}`)
  }

  async create(guide: IGuide): Promise<void> {
    /**
     * Create new Guide
     */
    await this.api.axios.post('guides', guide)
  }

  async approve(slug: string): Promise<void> {
    /**
     * Approve Guide by Slug
     */
    await this.api.axios.post(`guides/${slug}/approve`)
  }
}
