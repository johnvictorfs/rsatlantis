import Vue from 'vue';

export default {
  clanList() {
    return Vue.axios.get('/api/players/');
  }
};
