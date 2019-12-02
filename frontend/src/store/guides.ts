import { Module, MutationTree, ActionTree, GetterTree } from 'vuex'

import { GuideState, RootState } from './types'
import { IGuideWithAuthor } from '@/types'
import api from '@/api'

export const state: GuideState = {}

const actions: ActionTree<GuideState, RootState> = {
  publishGuide({ commit }, guideDetails: any) {
    return new Promise(async (resolve, reject) => {
      try {
        commit('SET_LOADING')
        const guides = await api.guides.create(guideDetails)
        resolve(guides)
      } catch (error) {
        reject(error)
      } finally {
        commit('REMOVE_LOADING')
      }
    })
  },
  guideList({ commit }): Promise<IGuideWithAuthor[]> {
    return new Promise(async (resolve, reject) => {
      try {
        commit('SET_LOADING')
        const guides = await api.guides.all()
        resolve(guides)
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
        const guide = await api.guides.get(slug)
        resolve(guide)
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
