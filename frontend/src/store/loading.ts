const state = {
  loading: false
};

const mutations = {
  SET_LOADING(state) {
    state.loading = true;
  },
  REMOVE_LOADING(state) {
    state.loading = false;
  }
};

const actions = {
  setLoading({ commit }) {
    commit('SET_LOADING');
  },
  removeLoading({ commit }) {
    commit('REMOVE_LOADING');
  }
};

export default {
  // namespaced: true,
  state,
  mutations,
  actions
};
