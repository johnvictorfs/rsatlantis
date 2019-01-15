import Vue from 'vue'
import Vuex from 'vuex'
import auth from './api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loading: false,
    theme: localStorage.getItem('THEME') || 'dark',
    token: localStorage.getItem('TOKEN') || null,
    username: localStorage.getItem('USERNAME') || '',
    ingameName: localStorage.getItem('INGAME_NAME') || '',
    email: localStorage.getItem('USER_EMAIL') | '',
    isAdmin: localStorage.getItem('IS_STAFF') | false,
    isSuperUser: localStorage.getItem('IS_SUPERUSER') | false,
    userUrl: localStorage.getItem('USER_URL') | '',
    userGuides: localStorage.getItem('USER_GUIDES') | '',
  },
  mutations: {
    SET_LOADING(state) {
      state.loading = true;
    },
    REMOVE_LOADING(state) {
      state.loading = false;
    },
    SET_THEME(state, theme) {
      state.theme = theme;
    },
    SET_TOKEN(state, token) {
      localStorage.setItem('TOKEN', token);
      Vue.axios.defaults.headers.common['Authorization'] = `Token ${token}`;
      state.token = token;
    },
    REMOVE_TOKEN(state) {
      localStorage.removeItem('TOKEN');
      delete Vue.axios.defaults.headers.common['Authorization'];
      state.token = null;
    },
    SET_ACCOUNT_DETAILS(state, details) {
      /** @namespace details.username **/
      /** @namespace details.ingame_name **/
      /** @namespace details.email **/
      /** @namespace details.is_staff **/
      /** @namespace details.is_superuser **/
      /** @namespace details.url **/
      /** @namespace details.guides **/
      localStorage.setItem('USERNAME', details.username);
      localStorage.setItem('INGAME_NAME', details.ingame_name);
      localStorage.setItem('USER_EMAIL', details.email);
      localStorage.setItem('IS_STAFF', details.is_staff);
      localStorage.setItem('IS_SUPERUSER', details.is_superuser);
      localStorage.setItem('USER_URL', details.url);
      localStorage.setItem('USER_GUIDES', details.guides);
      state.username = details.username;
      state.ingameName = details.ingame_name;
      state.email = details.email;
      state.isAdmin = details.is_staff;
      state.isSuperUser = details.is_superuser;
      state.userUrl = details.url;
      state.userGuides = details.guides;
    },
    CLEAR_ACCOUNT_DETAILS(state) {
      localStorage.removeItem('USERNAME');
      localStorage.removeItem('INGAME_NAME');
      localStorage.removeItem('USER_EMAIL');
      localStorage.removeItem('IS_STAFF');
      localStorage.removeItem('IS_SUPERUSER');
      localStorage.removeItem('USER_URL');
      localStorage.removeItem('USER_GUIDES');
      state.username = '';
      state.ingameName = '';
      state.email = '';
      state.isAdmin = false;
      state.isSuperUser = false;
      state.userUrl = '';
      state.userGuides = '';
    }
  },
  actions: {
    changeTheme({commit}, theme) {
      localStorage.setItem('THEME', theme);
      commit('SET_THEME', theme);
    },
    login({commit, dispatch}, credentials) {
      commit('SET_LOADING');
      return new Promise((resolve, reject) => {
        auth.login(credentials.username, credentials.password).then(response => {
          commit('SET_TOKEN', response.data.key);
          dispatch('accountDetails');
          commit('REMOVE_LOADING');
          resolve(response);
        }).catch(error => {
          commit('REMOVE_LOADING');
          reject(error);
        })
      });
    },
    logout({commit}) {
      commit('SET_LOADING');
      commit('REMOVE_TOKEN');
      commit('CLEAR_ACCOUNT_DETAILS');
      auth.logout();
      commit('REMOVE_LOADING');
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
    },
    createAccount({commit}, credentials) {
      commit('SET_LOADING');
      return new Promise((resolve, reject) => {
        auth.createAccount(credentials.username, credentials.password1, credentials.email, credentials.ingame_name).then(response => {
          commit('REMOVE_LOADING');
          resolve(response);
        }).catch(error => {
          commit('REMOVE_LOADING');
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