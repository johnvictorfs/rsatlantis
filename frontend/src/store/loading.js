const state = {
  loading: false,
};

const mutations = {
  SET_LOADING(state) {
    state.loading = true;
  },
  REMOVE_LOADING(state) {
    state.loading = false;
  },
};

export default {
  namespaced: true,
  state,
  mutations,
};