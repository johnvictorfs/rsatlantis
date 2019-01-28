const state = {
  theme: localStorage.getItem('THEME') || 'dark',
};

const mutations = {
  SET_THEME(state, theme) {
    state.theme = theme;
  },
};

const actions = {
  changeTheme({commit}, theme) {
    localStorage.setItem('THEME', theme);
    commit('SET_THEME', theme);
  },
};

const getters = {
  isDarkTheme: state => state.theme === 'dark',
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};