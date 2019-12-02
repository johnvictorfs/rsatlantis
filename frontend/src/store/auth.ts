import { Module, MutationTree, ActionTree, GetterTree } from 'vuex'

import { RootState, AuthState, ApiUserDetails, UserCredentials } from './types'
import api from '@/api'
import { IUser } from '@/types'

export const state: AuthState = {
  token: localStorage.getItem('TOKEN') || '',
  user: {
    username: '',
    ingameName: '',
    email: '',
    isAdmin: false,
    isSuperUser: false,
    userUrl: '',
    userGuides: ''
  }
}

export const mutations: MutationTree<AuthState> = {
  SET_TOKEN(state, token: string) {
    localStorage.setItem('TOKEN', token)
    state.token = token
  },
  REMOVE_TOKEN(state) {
    localStorage.removeItem('TOKEN')
    state.token = null
  },
  SET_ACCOUNT_DETAILS(state, details: ApiUserDetails) {
    state.user = {
      username: details.username,
      ingameName: details.ingame_name,
      email: details.email,
      isAdmin: details.is_staff,
      isSuperUser: details.is_superuser,
      userUrl: details.url,
      userGuides: details.guides
    }
  },
  CLEAR_ACCOUNT_DETAILS(state) {
    state.user = {
      username: '',
      ingameName: '',
      email: '',
      isAdmin: false,
      isSuperUser: false,
      userUrl: '',
      userGuides: ''
    }
  }
}

const actions: ActionTree<AuthState, RootState> = {
  login({ commit, dispatch }, credentials: UserCredentials) {
    return new Promise(async (resolve, reject) => {
      try {
        commit('SET_LOADING')
        const token = await api.users.login(credentials)

        commit('SET_TOKEN', token)
        dispatch('accountDetails')
        resolve(token)
      } catch (error) {
        reject(error)
      } finally {
        commit('REMOVE_LOADING')
      }
    })
  },
  async logout({ commit }) {
    try {
      commit('SET_LOADING')
      commit('REMOVE_TOKEN')
      commit('CLEAR_ACCOUNT_DETAILS')

      await api.users.logout()
    } catch (error) {} finally {
      commit('REMOVE_LOADING')
    }
  },
  accountDetails({ commit }) {
    return new Promise(async (resolve, reject) => {
      try {
        const user = await api.users.current()

        commit('SET_ACCOUNT_DETAILS', user)
        resolve(user)
      } catch (error) {
        reject(error)
      }
    })
  },
  createAccount({ commit }, credentials: IUser) {
    commit('SET_LOADING')
    return new Promise(async (resolve, reject) => {
      try {
        const user = await api.users.create(credentials)

        resolve(user)
      } catch (error) {
        reject(error)
      } finally {
        commit('REMOVE_LOADING')
      }
    })
  }
}

const getters: GetterTree<AuthState, RootState> = {
  isAuthenticated: (state): boolean => !!state.token
}

export const auth: Module<AuthState, RootState> = {
  state,
  getters,
  actions,
  mutations
}
