import auth from '../api/auth';
import api from '../api';

type State = {
  token: string | null;
  username: string;
  ingameName: string;
  email: string;
  isAdmin: boolean;
  isSuperUser: boolean;
  userUrl: string;
  userGuides: string;
};

const mutations = {
  SET_TOKEN(state: State, token: string) {
    localStorage.setItem('TOKEN', token);
    api.defaults.headers.common.Authorization = `Token ${token}`;
    state.token = token;
  },
  REMOVE_TOKEN(state: State) {
    localStorage.removeItem('TOKEN');
    delete api.defaults.headers.common.Authorization;
    state.token = null;
  },
  SET_ACCOUNT_DETAILS(state: State, details: any) {
    state.username = details.username;
    state.ingameName = details.ingame_name;
    state.email = details.email;
    state.isAdmin = details.is_staff;
    state.isSuperUser = details.is_superuser;
    state.userUrl = details.url;
    state.userGuides = details.guides;
  },
  CLEAR_ACCOUNT_DETAILS(state: State) {
    state.username = '';
    state.ingameName = '';
    state.email = '';
    state.isAdmin = false;
    state.isSuperUser = false;
    state.userUrl = '';
    state.userGuides = '';
  }
};

const actions = {
  login({ commit, dispatch }: { commit: any; dispatch: any }, credentials: any) {
    commit('SET_LOADING');
    return new Promise(async (resolve, reject) => {
      try {
        const response = await auth.login(credentials.username, credentials.password);
        commit('SET_TOKEN', response.data.key);
        dispatch('accountDetails');
        commit('REMOVE_LOADING');
        resolve(response);
      } catch (error) {
        commit('REMOVE_LOADING');
        reject(error);
      }
    });
  },
  logout({ commit }: { commit: any }) {
    commit('SET_LOADING');
    commit('REMOVE_TOKEN');
    commit('CLEAR_ACCOUNT_DETAILS');
    auth.logout();
    commit('REMOVE_LOADING');
  },
  accountDetails({ commit }: { commit: any }) {
    return new Promise(async (resolve, reject) => {
      try {
        const response = await auth.getAccountDetails();
        commit('SET_ACCOUNT_DETAILS', response.data);
        resolve(response);
      } catch (error) {
        reject(error);
      }
    });
  },
  createAccount({ commit }: { commit: any }, credentials: any) {
    commit('SET_LOADING');
    return new Promise(async (resolve, reject) => {
      try {
        const response = await auth.createAccount(credentials);
        resolve(response);
      } catch (error) {
        reject(error);
      } finally {
        commit('REMOVE_LOADING');
      }
    });
  }
};

const getters = {
  isAuthenticated(state: State): boolean {
    console.log(state);
    return !!state.token;
  }
};

export default {
  store: {
    token: localStorage.getItem('TOKEN') || '',
    username: '',
    ingameName: '',
    email: '',
    isAdmin: false,
    isSuperUser: false,
    userUrl: '',
    userGuides: ''
  },
  mutations,
  actions,
  getters
};
