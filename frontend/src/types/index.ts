export * from './users'
export * from './vapp'
export * from './guides'
export * from './players'
export * from './discord'

export type Nullable<T> = T | null;

type ClanType = 'off-game' | 'in-game'

export interface ClanEvent {
  id: number
  title: string
  type: ClanType | string
  image?: string | null
  beneficiente: boolean
  description?: string | null
  date: string
  organizer?: string | null
}
