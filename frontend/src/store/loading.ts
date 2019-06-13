import { Module, MutationTree, ActionTree } from 'vuex'

import { LoadingState, RootState } from './types'

const state: LoadingState = {
  loading: false
}

const mutations: MutationTree<LoadingState> = {
  SET_LOADING: state => state.loading = true,
  REMOVE_LOADING: state => state.loading = false
}

const actions: ActionTree<LoadingState, RootState> = {
  setLoading: ({ commit }) => commit('SET_LOADING'),
  removeLoading: ({ commit }) => commit('REMOVE_LOADING')
}

export const loading: Module<LoadingState, RootState> = {
  state,
  actions,
  mutations
}
