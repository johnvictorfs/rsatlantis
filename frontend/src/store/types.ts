export interface RootState {}

export interface User {
  username: string
  ingameName: string
  email: string
  isAdmin: boolean
  isSuperUser: boolean
  userUrl: string
  userGuides: string
}

export interface AuthState {
  user: User
}

export interface ApiUserDetails {
  username: string
  ingame_name: string
  email: string
  is_staff: boolean
  is_superuser: boolean
  url: string
  guides: string
}

export interface UserCredentials {
  username: string
  password: string
  password2?: string
  email?: string
  ingame_name?: string
}

export interface GuideState {}

export interface LoadingState {
  loading: boolean
}
