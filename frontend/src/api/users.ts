import Vue from 'vue'

import Service from '@/api/service'
import { Api } from '@/api'
import { IUser, IGuide } from '@/types'
import { formatError } from '@/helpers/errors'

export default class UserService extends Service {
  public async all(): Promise<IUser[]> {
    /**
     * Get all Users
     */
    const { data } = await this.api.axios.get('users')
    return data
  }

  public async get(id: number): Promise<IUser> {
    /**
     * Get specific User by ID
     */
    try {
      const { data } = await this.api.axios.get(`users/${id}`)
      return data
    } catch (error) {
      Vue.toasted.global.error('Erro ao atualizar informações de Guia')
      throw error
    }
  }

  public async delete(id: number): Promise<void> {
    /**
     * Delete User by ID
     */
    try {
      await this.api.axios.delete(`users/${id}`)
      Vue.toasted.global.success('Guia deletado com sucesso')
    } catch (error) {
      Vue.toasted.global.error(formatError(error))
    }
  }

  public async create(guide: IUser): Promise<void> {
    /**
     * Create new User
     */
    try {
      await this.api.axios.post('users', guide)
    } catch (error) {
      Vue.toasted.global.error(formatError(error))
    }
  }

  public async guides(id: number): Promise<IGuide[]> {
    /**
     * Get all Guides by specific User by ID
     */
    try {
      const { data } = await this.api.axios.get(`users/${id}/guides`)
      return data
    } catch (error) {
      Vue.toasted.global.error('Houve um erro ao atualizar informações de Guias')
      throw error
    }
  }

  public async login({ username, password }: { username: string, password: string }): Promise<string> {
    /**
     * User Login with Username and Password and add Token to localStorage
     */
    try {
      const { data } = await this.api.axios.post('auth/login', { username, password })

      localStorage.setItem('TOKEN', data.key)
      Vue.toasted.global.success('Você entrou na sua conta com sucesso!')

      return data.key
    } catch (error) {
      Vue.toasted.global.error(formatError(error))
      throw error
    }
  }

  public async logout(): Promise<void> {
    /**
     * Logout User and remove Token from localStorage
     */
    try {
      await this.api.axios.post('auth/logout')
      Vue.toasted.global.success('Você saiu da sua conta com sucesso')
    } catch (error) {
      Vue.toasted.global.error(formatError(error))
    }
  }

  async current(): Promise<IUser | null> {
    /**
     * Get information about current logged in User
     */
    try {
      const { data } = await this.api.axios.get('users/current')
      return data
    } catch (error) {
      return null
    }
  }
}
