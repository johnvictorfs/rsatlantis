import Vue from 'vue'
import Vuex, { StoreOptions } from 'vuex'

import { RootState } from './types'
import { auth } from './auth'
import { guides } from './guides'
import { loading } from './loading'

Vue.use(Vuex)

const store: StoreOptions<RootState> = {
  modules: {
    auth,
    guides,
    loading
  }
}

export default new Vuex.Store<RootState>(store)
