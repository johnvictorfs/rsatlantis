import { Module, MutationTree, ActionTree, GetterTree } from 'vuex'

import { GuideState, RootState } from './types'
import api from '../api'

export const state: GuideState = {}

const actions: ActionTree<GuideState, RootState> = {
  publishGuide({ commit }, guideDetails: any) {
    return new Promise(async (resolve, reject) => {
      try {
        commit('SET_LOADING')
        const response = await api.post('/api/guides/', guideDetails)
        resolve(response)
      } catch (error) {
        reject(error)
      } finally {
        commit('REMOVE_LOADING')
      }
    })
  },
  guideList({ commit }) {
    return new Promise(async (resolve, reject) => {
      try {
        commit('SET_LOADING')
        const response = await api.get('/api/guides/')
        resolve(response)
      } catch (error) {
        reject(error)
      } finally {
        commit('REMOVE_LOADING')
      }
    })
  },
  guideDetails({ commit }, slug: string) {
    return new Promise(async (resolve, reject) => {
      try {
        commit('SET_LOADING')
        const response = await api.get(`/api/guides/${slug}/`)
        resolve(response)
      } catch (error) {
        reject(error)
      } finally {
        commit('REMOVE_LOADING')
      }
    })
  }
}

export const guides: Module<GuideState, RootState> = {
  actions
}
