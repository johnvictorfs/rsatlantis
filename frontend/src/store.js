import Vue from 'vue'
import Vuex from 'vuex'
import auth from './api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    theme: localStorage.getItem('THEME') || 'dark',
    token: localStorage.getItem('TOKEN_STORAGE_KEY') || null,
    username: localStorage.getItem('USERNAME') || '',
    email: localStorage.getItem('USER_EMAIL') | '',
    isAdmin: localStorage.getItem('IS_STAFF') | false,
    isSuperUser: localStorage.getItem('IS_SUPERUSER') | false,
    user_url: localStorage.getItem('USER_URL') | '',
    user_guides: localStorage.getItem('USER_GUIDES') | '',
  },
  mutations: {
    SET_THEME(state, theme) {
      state.theme = theme;
    },
    SET_TOKEN(state, token) {
      localStorage.setItem('TOKEN_STORAGE_KEY', token);
      Vue.axios.defaults.headers.Authorization = `Token ${token}`;
      state.token = token;
    },
    REMOVE_TOKEN(state) {
      localStorage.removeItem('TOKEN_STORAGE_KEY');
      delete Vue.axios.defaults.headers.Authorization;
      state.token = null;
    },
    SET_ACCOUNT_DETAILS(state, details) {
      /** @namespace details.username **/
      /** @namespace details.email **/
      /** @namespace details.is_staff **/
      /** @namespace details.is_superuser **/
      /** @namespace details.url **/
      /** @namespace details.guides **/
      localStorage.setItem('USERNAME', details.username);
      localStorage.setItem('USER_EMAIL', details.email);
      localStorage.setItem('IS_STAFF', details.is_staff);
      localStorage.setItem('IS_SUPERUSER', details.is_superuser);
      localStorage.setItem('USER_URL', details.url);
      localStorage.setItem('USER_GUIDES', details.guides);
      state.username = details.username;
      state.email = details.email;
      state.isAdmin = details.is_staff;
      state.isSuperUser = details.is_superuser;
      state.user_url = details.url;
      state.user_guides = details.guides;
    },
    CLEAR_ACCOUNT_DETAILS(state) {
      localStorage.removeItem('USERNAME');
      localStorage.removeItem('USER_EMAIL');
      localStorage.removeItem('IS_STAFF');
      localStorage.removeItem('IS_SUPERUSER');
      localStorage.removeItem('USER_URL');
      localStorage.removeItem('USER_GUIDES');
      state.username = '';
      state.email = '';
      state.isAdmin = false;
      state.isSuperUser = false;
      state.user_url = '';
      state.user_guides = '';
    }
  },
  actions: {
    changeTheme({commit}, theme) {
      localStorage.setItem('THEME', theme);
      commit('SET_THEME', theme);
    },
    login({commit, dispatch}, credentials) {
      return new Promise((resolve, reject) => {
        auth.login(credentials.username, credentials.password).then(response => {
          commit('SET_TOKEN', response.data.key);
          dispatch('accountDetails');
          resolve(response);
        }).catch(error => {
          reject(error);
        })
      });
    },
    logout({commit}) {
      commit('REMOVE_TOKEN');
      commit('CLEAR_ACCOUNT_DETAILS');
      auth.logout();
    },
    accountDetails({commit}) {
      return new Promise((resolve, reject) => {
        auth.getAccountDetails().then(response => {
          commit('SET_ACCOUNT_DETAILS', response.data);
          resolve(response);
        }).catch(error => {
          reject(error);
        })
      })
    }
  },
  getters: {
    isDarkTheme: state => state.theme === 'dark',
    isAuthenticated: state => !!state.token
  }
})