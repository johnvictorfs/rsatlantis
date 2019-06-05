import guide from '../api/guide';

const actions = {
  publishGuide({ commit }: { commit: any }, guideDetails: any) {
    commit('SET_LOADING');
    return new Promise((resolve, reject) => {
      guide
        .publishGuide(guideDetails)
        .then(response => {
          resolve(response);
        })
        .catch(error => {
          reject(error);
        })
        .finally(() => {
          commit('REMOVE_LOADING');
        });
    });
  },
  guideList({ commit }: { commit: any }) {
    commit('SET_LOADING');
    return new Promise((resolve, reject) => {
      guide
        .guideList()
        .then(response => {
          resolve(response);
        })
        .catch(error => {
          reject(error);
        })
        .finally(() => {
          commit('REMOVE_LOADING');
        });
    });
  },
  guideDetails({ commit }: { commit: any }, slug: string) {
    commit('SET_LOADING');
    return new Promise((resolve, reject) => {
      guide
        .guideDetails(slug)
        .then(response => {
          resolve(response);
        })
        .catch(error => {
          reject(error);
        })
        .finally(() => {
          commit('REMOVE_LOADING');
        });
    });
  }
};

export default {
  actions
};
