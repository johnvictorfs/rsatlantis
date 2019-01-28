import Vue from 'vue'
import Vuex from 'vuex'


import auth from './auth'
import guides from './guides'
import loading from './loading'
import sidebar from './sidebar'
import theme from './theme'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    guides,
    loading,
    sidebar,
    theme
  }
});