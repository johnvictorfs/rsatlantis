import Vue from 'vue'


export function isInClan(player) {
  /** @namespace response.data.clan **/
  return new Promise((resolve, reject) => {
    Vue.axios({
      url: `http://services.runescape.com/m=website-data/playerDetails.ws?names=%5B%22${player}%22%5D&callback=jQuery000000000000000_0000000000&_=0`,
      headers: {},
      method: 'get'
    }).then(response => {
      resolve(response.data.clan === 'Atlantis');
    }).catch(error => {
      reject(error)
    });
  });
}
