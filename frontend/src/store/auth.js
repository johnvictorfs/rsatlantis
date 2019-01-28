import auth from '../api/auth'
import Vue from "vue";

const state = {
  token: localStorage.getItem('TOKEN') || null,
  username: '',
  ingameName: '',
  email: '',
  isAdmin: false,
  isSuperUser: false,
  userUrl: '',
  userGuides: '',
};

const mutations = {
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
    state.username = details.username;
    state.ingameName = details.ingame_name;
    state.email = details.email;
    state.isAdmin = details.is_staff;
    state.isSuperUser = details.is_superuser;
    state.userUrl = details.url;
    state.userGuides = details.guides;
  },
  CLEAR_ACCOUNT_DETAILS(state) {
    state.username = '';
    state.ingameName = '';
    state.email = '';
    state.isAdmin = false;
    state.isSuperUser = false;
    state.userUrl = '';
    state.userGuides = '';
  },
};

const actions = {
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
      auth.createAccount(credentials).then(response => {
        resolve(response);
      }).catch(error => {
        reject(error);
      }).finally(() => {
        commit('REMOVE_LOADING');
      })
    })
  },
};

const getters = {
  isAuthenticated: state => !!state.token
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};