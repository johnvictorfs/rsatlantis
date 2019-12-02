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
