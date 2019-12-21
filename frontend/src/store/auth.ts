import { Module, MutationTree, ActionTree, GetterTree } from 'vuex'

import { RootState, AuthState, ApiUserDetails, UserCredentials } from './types'
import api from '@/api'
import { IUser } from '@/types'

export const state: AuthState = {
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
        await api.users.login(credentials)
        dispatch('accountDetails')
        resolve()
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
      commit('CLEAR_ACCOUNT_DETAILS')

      await api.users.logout()
    } catch (error) {} finally {
      commit('REMOVE_LOADING')
    }
  },
  accountDetails({ commit }) {
    return new Promise(async (resolve, reject) => {
      /**
       * Set or Clear User's account details based on if
       * he is logged in or not
       */
      try {
        const user = await api.users.current()
        if (user) {
          commit('SET_ACCOUNT_DETAILS', user)
        } else {
          commit('CLEAR_ACCOUNT_DETAILS')
        }
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
  isAuthenticated: (state): boolean => !!(state.user && state.user.username),
  isAdmin: (state): boolean => !!(state.user && state.user.isAdmin),
  isSuperUser: (state): boolean => !!(state.user && state.user.isSuperUser)
}

export const auth: Module<AuthState, RootState> = {
  state,
  getters,
  actions,
  mutations
}
