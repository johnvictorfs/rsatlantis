type State = {
  loading: boolean;
};

const state: State = {
  loading: false
};

const mutations = {
  SET_LOADING(state: State) {
    state.loading = true;
  },
  REMOVE_LOADING(state: State) {
    state.loading = false;
  }
};

const actions = {
  setLoading({ commit }: { commit: any }) {
    commit('SET_LOADING');
  },
  removeLoading({ commit }: { commit: any }) {
    commit('REMOVE_LOADING');
  }
};

export default {
  // namespaced: true,
  state,
  mutations,
  actions
};
