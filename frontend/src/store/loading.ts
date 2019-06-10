import { Module, MutationTree, ActionTree } from 'vuex'

import { LoadingState, RootState } from './types'

const state: LoadingState = {
  loading: false
}

const mutations: MutationTree<LoadingState> = {
  SET_LOADING(state) {
    state.loading = true
  },
  REMOVE_LOADING(state) {
    state.loading = false
  }
}

const actions: ActionTree<LoadingState, RootState> = {
  setLoading({ commit }: { commit: any }) {
    commit('SET_LOADING')
  },
  removeLoading({ commit }: { commit: any }) {
    commit('REMOVE_LOADING')
    setTimeout(() => commit('REMOVE_LOADING'), 5000)
  }
}

export const loading: Module<LoadingState, RootState> = {
  state,
  actions,
  mutations
}
