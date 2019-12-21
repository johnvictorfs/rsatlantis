export interface IPlayer {
  url: string
  name: string
  exp: number | string
  rank: Rank
  translated_rank: TranslatedRank
}

type Rank = 'Owner' | 'Deputy Owner' | 'Overseer' | 'Coordinator' | 'Organiser' | 'Admin' | 'General' | 'Captain' | 'Lieutenant' | 'Sergeant' | 'Corporal' | 'Recruit'
type TranslatedRank = 'Líder' | 'Fiscal' | 'Coordenador' | 'Organizador' | 'Administrador' | 'General' | 'Capitão' | 'Tenente' | 'Sargento' | 'Cabo' | 'Recruta'
