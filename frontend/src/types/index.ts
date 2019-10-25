export interface IAuthor {
  isAdmin: boolean
  isSuperUser: boolean
}

export interface IGuideFields {
  url: string
  title: string
  slug: string
  category: string
  description: string
  content: string
  approved: boolean
  date_posted: string
}

export interface IGuide extends IGuideFields {
  author: IAuthor
}

export interface IApiGuide extends IGuideFields {
  author: string
}

export interface IApiUser {
  url: string
  guides: string
  username: string
  ingame_name: string
  email: string
  groups: string[]
  is_staff: boolean
  is_superuser: boolean
}

export interface RouterPath {
  name: string
}

export interface ToolbarItem {
  text: string
  path: RouterPath
  color: string
  auth: boolean | 'any'
  icon: string
}
