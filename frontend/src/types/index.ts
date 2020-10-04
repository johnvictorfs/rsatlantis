export * from './users'
export * from './vapp'
export * from './guides'
export * from './players'
export * from './discord'

export type Nullable<T> = T | null;

export interface ClanEvent {
  id: number
  title: string
  type: 'off-game' | 'in-game'
  image: string
  beneficiente: boolean
  description?: string
  date: Date
  organizer?: string
}
