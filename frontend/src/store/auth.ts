import { Module, MutationTree, ActionTree, GetterTree } from 'vuex'

import { RootState, AuthState, ApiUserDetails, UserCredentials } from './types'
import api from '@/api'

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
    api.defaults.headers.common.Authorization = `Token ${token}`
    state.token = token
  },
  REMOVE_TOKEN(state) {
    localStorage.removeItem('TOKEN')
    delete api.defaults.headers.common.Authorization
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
        const { username, password } = credentials

        const response = await api.post('auth/login', { username, password })

        commit('SET_TOKEN', response.data.key)
        dispatch('accountDetails')
        resolve(response)
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

      await api.post('auth/logout', {})
    } catch (error) {} finally {
      commit('REMOVE_LOADING')
    }
  },
  accountDetails({ commit }) {
    return new Promise(async (resolve, reject) => {
      try {
        const response = await api.get('users/current')

        commit('SET_ACCOUNT_DETAILS', response.data)

        resolve(response)
      } catch (error) {
        reject(error)
      }
    })
  },
  createAccount({ commit }, credentials: UserCredentials) {
    commit('SET_LOADING')
    return new Promise(async (resolve, reject) => {
      try {
        const response = await api.post('users', credentials)

        resolve(response)
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
