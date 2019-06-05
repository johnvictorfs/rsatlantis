import api from '.';

export default {
  clanList() {
    return api.get('/api/players/');
  }
};
