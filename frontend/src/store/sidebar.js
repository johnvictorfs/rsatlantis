const state = {
  sidebar: false,
};

const mutations = {
  TOGGLE_SIDEBAR_ON(state) {
    state.sidebar = true;
  },
  TOGGLE_SIDEBAR_OFF(state) {
    state.sidebar = false;
  }
};

const actions = {
  toggleSideBarOff({commit}) {
    commit('TOGGLE_SIDEBAR_OFF')
  },
  toggleSideBarOn({commit}) {
    commit('TOGGLE_SIDEBAR_ON')
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions
};