import { IUser } from '@/types'

export type GuideCategory = '' | 'PvM' | 'pvm' | 'Habilidades' | 'skilling' | 'Outros' | 'others'

export interface IAuthor {
  isAdmin: boolean
  isSuperUser: boolean
}

export interface IGuide {
  url?: string
  title: string
  slug?: string
  category: GuideCategory
  description: string
  content: string
  approved?: boolean
  date_posted?: string
  author?: IAuthor | string
}

export interface IGuideWithAuthor extends IGuide {
  getAuthor: () => Promise<IUser | null>
}
